"""Used by the `config` module to load the config options"""

from __future__ import annotations

__all__ = (
    'FlaskCeleryOption', 'Option', 'CELERY_OPTIONS', 'FLASK_OPTIONS', 'OPTIONS'
)

import os
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any, Final, Optional

_DEFAULT: Final = object()


def _convert_env_var(value: str, type_: type, env_var: str) -> Any:
    """Convert the given env-var string to the correct type"""
    if type_ is str:
        return value
    elif type_ is bool:
        value = value.lower()
        if value in {'true', 't', '1', 'yes', 'y'}:
            return True
        elif value in {'false', 'f', '0', 'no', 'n'}:
            return False
        else:
            raise ValueError(
                f'The environment variable {env_var} has an invalid value:'
                f" {value!r}. Expected 'TRUE' or 'FALSE'"
            )
    elif type_ is list:
        return value.split(',')
    else:
        try:
            return type_(value)
        except Exception as e:
            raise ValueError(
                f'The environment variable {env_var} has an invalid value:'
                f' {value!r}. Expected an {type_.__name__}'
            ) from e


@dataclass(frozen=True)
class Option:
    """Individual config options used by `OPTIONS`"""

    name: str
    """Name of the option that will be used in the `config.Config` class"""
    type: type
    """Type of the option as found in the config file

    See `value_converter` if you want to change the type of the option
    after loading it
    """
    # The value is set to the correct type in `__post_init__()`
    config_key: tuple[str, ...] = None  # type: ignore[assignment]
    """Location of the option within the config file

    Multiple values represents a nested mapping. For example, a value
    of `('foo',)` represents the key 'foo' in the top-level mapping,
    while a value of `('foo', 'bar')` represents the key 'bar' within
    the mapping 'foo'

    Defaults to a tuple containing only `name`
    """
    env_var: Optional[str] = None
    """Environment var that the option will be loaded from if it exists

    The env var has priority over the value in the config file
    """
    default: Any = _DEFAULT
    """Default value of the option if it isn't found in the config file
    or as an env var"""
    default_factory: Optional[Callable[[], Any]] = None
    """Same as `default`, but the value is generated by calling this
    function

    Use this instead of `default` if the default value is mutable
    """
    required: bool = field(init=False)
    """Whether or not the option is required

    This is automatically set to `True` if either `default` or
    `default_factory` is defined
    """

    value_converter: Optional[Callable[[Any], Any]] = None
    """The value of the option will be passed through this function if
    defined

    For example, you can convert a list to a tuple by setting this to
    `tuple`

    See `convert_value()` for details

    Note: this function isn't used if the option is set to the default
    value
    """

    def __post_init__(self) -> None:
        if self.default is not _DEFAULT and self.default_factory is not None:
            raise ValueError(
                f'Conflicting options for {self.name!r}.'
                " Only one of 'default' or 'default_factory' can be defined"
            )

        required = self.default is _DEFAULT and self.default_factory is None
        object.__setattr__(self, 'required', required)

        if self.config_key is None:
            object.__setattr__(self, 'config_key', (self.name,))

    def get_default(self) -> Any:
        """Return the default value of the option

        Raises an error if the option is required
        """
        if self.required:
            raise RuntimeError(
                f'The option {self.name!r} does not have a default value'
            )
        if self.default is not _DEFAULT:
            return self.default
        else:
            # Ignore error about `None` not being callable, because
            # `default_factory` will never be `None` when this
            # else-statement runs
            return self.default_factory()  # type: ignore[misc]

    def convert_value(self, value: Any) -> Any:
        """Convert value of the option using `value_converter()`

        If `value_converter()` isn't defined, the value will be returned
        as-is
        """
        if self.value_converter is not None:
            return self.value_converter(value)
        else:
            return value

    def nested_in(
        self, dict_: Mapping[Any, Any], *, assert_type: bool = True
    ) -> bool:
        """Recursively check if the option is contained in the given
        config mapping

        If `assert_type` is `True`, an error will be raised if an
        intermediate mapping is the wrong type. Otherwise, it will just
        return `False`
        """
        for level in self.config_key:
            if not isinstance(dict_, Mapping):
                if assert_type:
                    raise TypeError(
                        f'The config option {".".join(self.config_key)!r} has '
                        'an invalid type. Expected a mapping, '
                        f'not a {type(dict_).__name__}'
                    )
                else:
                    return False
            if level not in dict_:
                return False
            dict_ = dict_[level]
        return True

    def nested_get(self, dict_: Mapping[Any, Any]) -> Any:
        """Recursively get the option from the config mapping"""
        for level in self.config_key:
            dict_ = dict_[level]
        # `dict_` is actually the value when the loop finishes
        return dict_

    def get_env(self, mapping: Optional[Mapping[str, str]] = None) -> Any:
        """Retrieve the option from the given env-var mapping

        The value will be converted from a str to the correct type.

        `mapping` defaults to `os.environ` when `None`.
        """
        if mapping is None:
            mapping = os.environ

        if self.env_var is None:
            raise RuntimeError(
                f'The option {self.name!r} does not have an env-var set'
            )

        value = mapping[self.env_var]
        return _convert_env_var(value, self.type, self.env_var)


@dataclass(frozen=True)
class FlaskCeleryOption:
    """Individual Flask-or-Celery config options used by `FLASK_OPTIONS`
    and `CELERY_OPTIONS`"""

    name: str
    """Name of the Flask/Celery option"""
    env_var: str
    """Environment var that the option will be loaded from if it exists"""
    type: type
    """Type of the option

    The option will be converted to this type
    """

    def get_env(self, mapping: Optional[Mapping[str, str]] = None) -> Any:
        """Retrieve the option from the given env-var mapping

        The value will be converted from a str to the correct type

        `mapping` defaults to `os.environ` when `None`.
        """
        if mapping is None:
            mapping = os.environ

        value = mapping[self.env_var]
        return _convert_env_var(value, self.type, self.env_var)


OPTIONS: Final = (
    Option(name='database_uri', env_var='YTDL_DATABASE_URI', type=str),
    Option(name='flask_config', type=dict, default_factory=dict),
    Option(name='celery_config', type=dict, default_factory=dict),
    # The download dir defaults to the working dir of the API (not the
    # worker) since it's passed as an arg to `task.download`.
    #
    # It's done this way because the API needs to know the download_dir
    # in order to check the value of `outtmpl`.
    Option(
        name='download_dir', env_var='YTDL_DOWNLOAD_DIR', type=str,
        default_factory=os.getcwd
    ),
    Option(
        name='force_download_dir', env_var='YTDL_FORCE_DOWNLOAD_DIR',
        type=bool, default=True
    ),
    Option(
        name='allow_user_opts', env_var='YTDL_ALLOW_USER_OPTS',
        type=bool, default=True
    ),
    Option(
        name='ytdl_default_opts', config_key=('ytdl_opts', 'default_opts'),
        type=dict, default_factory=dict
    ),
    Option(
        name='ytdl_enable_whitelist', env_var='YTDL_ENABLE_WHITELIST',
        config_key=('ytdl_opts', 'enable_whitelist'), type=bool,
        default=True
    ),
    Option(
        name='ytdl_whitelist', env_var='YTDL_WHITELIST',
        config_key=('ytdl_opts', 'whitelist'), type=list,
        # TODO: add support for match_filter (requires a custom_opt).
        value_converter=frozenset, default=frozenset((
            'age_limit', 'allsubtitles', 'ap_mso', 'ap_password',
            'ap_username', 'buffersize', 'continuedl', 'default_search',
            'fixup', 'force_generic_extractor', 'format', 'geo_bypass',
            'geo_bypass_country', 'geo_bypass_ip_block', 'hls_use_mpegts',
            'http_chunk_size', 'ignoreerrors', 'include_ads', 'keepvideo',
            'matchtitle', 'max_filesize', 'max_sleep_interval',
            'max_views', 'merge_output_format', 'min_filesize',
            'min_views', 'nooverwrites', 'nopart', 'noplaylist',
            'noresizebuffer', 'outtmpl', 'outtmpl_na_placeholder',
            'password', 'playlistend', 'playlist_items', 'playlistrandom',
            'playlistreverse', 'playliststart', 'ratelimit', 'rejecttitle',
            'restrictfilenames', 'retries', 'simulate', 'skip_download',
            'sleep_interval', 'subtitlesformat', 'subtitleslangs',
            'updatetime', 'username', 'videopassword',
            'write_all_thumbnails', 'writeannotations',
            'writeautomaticsub', 'writedescription', 'writeinfojson',
            'writesubtitles', 'writethumbnail', 'xattr_set_filesize',
            'youtube_include_dash_manifest',
            # yt-dlp options
            # TODO: Add support for 'paths'. It allows downloading to
            #       other locations, so will need to be checked
            #       similarily to 'outtmpl'
            'allow_multiple_audio_streams', 'allow_multiple_video_streams',
            'allow_playlist_files', 'break_on_existing', 'break_on_reject',
            'check_formats', 'dynamic_mpd', 'extractor_retries',
            'force_write_download_archive', 'final_ext', 'format_sort',
            'format_sort_force', 'fragment_retries', 'getcomments',
            'hls_split_discontinuity', 'ignore_no_formats_error', 'overwrites',
            'skip_playlist_after_errors', 'sleep_interval_requests',
            'sleep_interval_subtitles', 'throttledratelimit', 'trim_file_name',
            'windowsfilenames', 'writedesktoplink', 'writeurllink',
            'writewebloclink', 'youtube_include_hls_manifest'
        ))
    ),
    Option(
        name='ytdl_whitelist_add', env_var='YTDL_WHITELIST_ADD',
        config_key=('ytdl_opts', 'whitelist_add'), type=list,
        value_converter=frozenset, default=frozenset()
    ),
    Option(
        name='ytdl_whitelist_remove', env_var='YTDL_WHITELIST_REMOVE',
        config_key=('ytdl_opts', 'whitelist_remove'), type=list,
        value_converter=frozenset, default=frozenset()
    ),
    Option(
        name='ytdl_sensitive_opts', env_var='YTDL_SENSITIVE_OPTS',
        config_key=('ytdl_opts', 'sensitive_opts'), type=list,
        value_converter=tuple,
        default=('ap_password', 'password', 'videopassword')
    ),
    Option(
        name='custom_default_opts', config_key=('custom_opts', 'default_opts'),
        type=dict, default_factory=dict
    ),
    Option(
        name='custom_enable_whitelist',
        env_var='YTDL_ENABLE_CUSTOM_WHITELIST',
        config_key=('custom_opts', 'enable_whitelist'), type=bool,
        default=False
    ),
    Option(
        name='custom_whitelist', env_var='YTDL_CUSTOM_WHITELIST',
        config_key=('custom_opts', 'whitelist'), type=list,
        value_converter=frozenset, default=frozenset()
    ),
    Option(
        name='ytdl_module', env_var='YTDL_MODULE', type=str,
        default='youtube_dl'
    ),
    Option(
        name='ytdl_class', env_var='YTDL_CLASS', type=str,
        default='YoutubeDL'
    ),
    Option(
        name='daterange_module', env_var='YTDL_DATERANGE_MODULE', type=str,
        default=None
    ),
    Option(
        name='daterange_class', env_var='YTDL_DATERANGE_CLASS', type=str,
        default='DateRange'
    ),
    Option(
        name='metadata_module', env_var='YTDL_METADATA_MODULE', type=str,
        default=None
    ),
    Option(
        name='metadata_class', env_var='YTDL_METADATA_CLASS', type=str,
        default='MetadataParserPP'
    )
)
"""List of config options that will be loaded in `config.Config`"""

FLASK_OPTIONS: Final = (
    FlaskCeleryOption(
        name='SERVER_NAME', env_var='YTDL_FLASK_SERVER_NAME', type=str
    ),
    FlaskCeleryOption(
        name='APPLICATION_ROOT', env_var='YTDL_FLASK_APPLICATION_ROOT',
        type=str
    ),
    FlaskCeleryOption(
        name='PREFERRED_URL_SCHEME',
        env_var='YTDL_FLASK_PREFERRED_URL_SCHEME', type=str
    ),
    FlaskCeleryOption(
        name='MAX_CONTENT_LENGTH', env_var='YTDL_FLASK_MAX_CONTENT_LENGTH',
        type=int
    ),
    FlaskCeleryOption(
        name='JSON_AS_ASCII', env_var='YTDL_FLASK_JSON_AS_ASCII', type=bool
    ),
    FlaskCeleryOption(
        name='JSON_SORT_KEYS', env_var='YTDL_FLASK_JSON_SORT_KEYS',
        type=bool
    ),
    FlaskCeleryOption(
        name='JSONIFY_PRETTYPRINT_REGULAR',
        env_var='YTDL_FLASK_JSONIFY_PRETTYPRINT_REGULAR', type=bool
    ),
    FlaskCeleryOption(
        name='JSONIFY_MIMETYPE', env_var='YTDL_FLASK_JSONIFY_MIMETYPE',
        type=str
    )
)
"""List of Flask env-var options that will be added to
`config.Config.flask_config`"""

CELERY_OPTIONS: Final = (
    FlaskCeleryOption(
        name='enable_utc', env_var='YTDL_CELERY_ENABLE_UTC', type=bool
    ),
    FlaskCeleryOption(
        name='timezone', env_var='YTDL_CELERY_TIMEZONE', type=str
    ),
    FlaskCeleryOption(
        name='task_compression', env_var='YTDL_CELERY_TASK_COMPRESSION',
        type=str
    ),
    FlaskCeleryOption(
        name='task_protocol', env_var='YTDL_CELERY_TASK_PROTOCOL', type=int
    ),
    FlaskCeleryOption(
        name='task_publish_retry',
        env_var='YTDL_CELERY_TASK_PUBLISH_RETRY', type=bool
    ),
    FlaskCeleryOption(
        name='task_soft_time_limit',
        env_var='YTDL_CELERY_TASK_SOFT_TIME_LIMIT', type=int
    ),
    FlaskCeleryOption(
        name='task_acks_late', env_var='YTDL_CELERY_TASK_ACKS_LATE',
        type=bool
    ),
    FlaskCeleryOption(
        name='task_acks_on_failure_or_timeout',
        env_var='YTDL_CELERY_TASK_ACKS_ON_FAILURE_OR_TIMEOUT', type=bool
    ),
    FlaskCeleryOption(
        name='task_reject_on_worker_lost',
        env_var='YTDL_CELERY_TASK_REJECT_ON_WORKER_LOST', type=bool
    ),
    FlaskCeleryOption(
        name='task_default_rate_limit',
        env_var='YTDL_CELERY_TASK_DEFAULT_RATE_LIMIT', type=int
    ),
    # 'result_backend' is automatically set to the same value as
    # `database_uri` when it's not explicitly given
    FlaskCeleryOption(
        name='result_backend', env_var='YTDL_CELERY_RESULT_BACKEND',
        type=str
    ),
    FlaskCeleryOption(
        name='result_backend_always_retry',
        env_var='YTDL_CELERY_RESULT_BACKEND_ALWAYS_RETRY', type=bool
    ),
    FlaskCeleryOption(
        name='result_backend_max_sleep_between_retries_ms',
        env_var='YTDL_CELERY_RESULT_BACKEND_MAX_SLEEP_BETWEEN_RETRIES_MS',
        type=int
    ),
    FlaskCeleryOption(
        name='result_backend_base_sleep_between_retries_ms',
        env_var='YTDL_CELERY_RESULT_BACKEND_BASE_SLEEP_BETWEEN_RETRIES_MS',
        type=int
    ),
    FlaskCeleryOption(
        name='result_backend_max_retries',
        env_var='YTDL_CELERY_RESULT_BACKEND_MAX_RETRIES', type=int
    ),
    FlaskCeleryOption(
        name='result_compression',
        env_var='YTDL_CELERY_RESULT_COMPRESSION', type=str
    ),
    FlaskCeleryOption(
        name='result_expires', env_var='YTDL_CELERY_RESULT_EXPIRES',
        type=int
    ),
    FlaskCeleryOption(
        name='result_chord_join_timeout',
        env_var='YTDL_CELERY_RESULT_CHORD_JOIN_TIMEOUT', type=float
    ),
    FlaskCeleryOption(
        name='result_chord_retry_interval',
        env_var='YTDL_CELERY_RESULT_CHORD_RETRY_INTERVAL', type=float
    ),
    FlaskCeleryOption(
        name='database_short_lived_sessions',
        env_var='YTDL_CELERY_DATABASE_SHORT_LIVED_SESSIONS', type=bool
    ),
    FlaskCeleryOption(
        name='broker_url', env_var='YTDL_CELERY_BROKER_URL', type=str
    ),
    FlaskCeleryOption(
        name='broker_read_url', env_var='YTDL_CELERY_BROKER_READ_URL',
        type=str
    ),
    FlaskCeleryOption(
        name='broker_write_url', env_var='YTDL_CELERY_BROKER_WRITE_URL',
        type=str
    ),
    FlaskCeleryOption(
        name='broker_failover_strategy',
        env_var='YTDL_CELERY_BROKER_FAILOVER_STRATEGY', type=str
    ),
    FlaskCeleryOption(
        name='broker_heartbeat', env_var='YTDL_CELERY_BROKER_HEARTBEAT',
        type=float
    ),
    FlaskCeleryOption(
        name='broker_heartbeat_checkrate',
        env_var='YTDL_CELERY_BROKER_HEARTBEAT_CHECKRATE', type=float
    ),
    FlaskCeleryOption(
        name='broker_pool_limit', env_var='YTDL_CELERY_BROKER_POOL_LIMIT',
        type=int
    ),
    FlaskCeleryOption(
        name='broker_connection_timeout',
        env_var='YTDL_CELERY_BROKER_CONNECTION_TIMEOUT', type=float
    ),
    FlaskCeleryOption(
        name='broker_connection_retry',
        env_var='YTDL_CELERY_BROKER_CONNECTION_RETRY', type=bool
    ),
    FlaskCeleryOption(
        name='broker_connection_max_retries',
        env_var='YTDL_CELERY_BROKER_CONNECTION_MAX_RETRIES', type=int
    ),
    FlaskCeleryOption(
        name='broker_login_method',
        env_var='YTDL_CELERY_BROKER_LOGIN_METHOD', type=str
    ),
    FlaskCeleryOption(
        name='worker_concurrency',
        env_var='YTDL_CELERY_WORKER_CONCURRENCY', type=int
    ),
    FlaskCeleryOption(
        name='worker_prefetch_multiplier',
        env_var='YTDL_CELERY_WORKER_PREFETCH_MULTIPLIER', type=int
    ),
    FlaskCeleryOption(
        name='worker_lost_wait', env_var='YTDL_CELERY_WORKER_LOST_WAIT',
        type=float
    ),
    FlaskCeleryOption(
        name='worker_max_tasks_per_child',
        env_var='YTDL_CELERY_WORKER_MAX_TASKS_PER_CHILD', type=int
    ),
    FlaskCeleryOption(
        name='worker_max_memory_per_child',
        env_var='YTDL_CELERY_WORKER_MAX_MEMORY_PER_CHILD', type=int
    ),
    FlaskCeleryOption(
        name='worker_disable_rate_limits',
        env_var='YTDL_CELERY_WORKER_DISABLE_RATE_LIMITS', type=bool
    ),
    FlaskCeleryOption(
        name='worker_state_db', env_var='YTDL_CELERY_WORKER_STATE_DB',
        type=str
    ),
    FlaskCeleryOption(
        name='worker_timer_precision',
        env_var='YTDL_CELERY_WORKER_TIMER_PRECISION', type=float
    ),
    FlaskCeleryOption(
        name='worker_enable_remote_control',
        env_var='YTDL_CELERY_WORKER_ENABLE_REMOTE_CONTROL', type=bool
    ),
    FlaskCeleryOption(
        name='worker_proc_alive_timeout',
        env_var='YTDL_CELERY_WORKER_PROC_ALIVE_TIMEOUT', type=float
    ),
    FlaskCeleryOption(
        name='worker_cancel_long_running_tasks_on_connection_loss',
        env_var=(
            'YTDL_CELERY_'
            'WORKER_CANCEL_LONG_RUNNING_TASKS_ON_CONNECTION_LOSS'
        ),
        type=bool
    ),
    FlaskCeleryOption(
        name='worker_send_task_events',
        env_var='YTDL_CELERY_WORKER_SEND_TASK_EVENTS', type=bool
    ),
    FlaskCeleryOption(
        name='task_send_sent_event',
        env_var='YTDL_CELERY_TASK_SEND_SENT_EVENT', type=bool
    ),
    FlaskCeleryOption(
        name='event_queue_ttl',
        env_var='YTDL_CELERY_EVENT_QUEUE_TTL', type=float
    ),
    FlaskCeleryOption(
        name='event_queue_expires',
        env_var='YTDL_CELERY_EVENT_QUEUE_EXPIRES', type=float
    ),
    FlaskCeleryOption(
        name='event_queue_prefix',
        env_var='YTDL_CELERY_EVENT_QUEUE_PREFIX', type=str
    ),
    FlaskCeleryOption(
        name='event_exchange', env_var='YTDL_CELERY_EVENT_EXCHANGE',
        type=str
    ),
    FlaskCeleryOption(
        name='control_queue_ttl', env_var='YTDL_CELERY_CONTROL_QUEUE_TTL',
        type=float
    ),
    FlaskCeleryOption(
        name='control_queue_expires',
        env_var='YTDL_CELERY_CONTROL_QUEUE_EXPIRES', type=float
    ),
    FlaskCeleryOption(
        name='control_exchange', env_var='YTDL_CELERY_CONTROL_EXCHANGE',
        type=str
    ),
    FlaskCeleryOption(
        name='worker_log_color', env_var='YTDL_CELERY_WORKER_LOG_COLOR',
        type=bool
    ),
    FlaskCeleryOption(
        name='worker_log_format', env_var='YTDL_CELERY_WORKER_LOG_FORMAT',
        type=str
    ),
    FlaskCeleryOption(
        name='worker_task_log_format',
        env_var='YTDL_CELERY_WORKER_TASK_LOG_FORMAT', type=str
    ),
    FlaskCeleryOption(
        name='beat_schedule_filename',
        env_var='YTDL_CELERY_BEAT_SCHEDULE_FILENAME', type=str
    ),
    FlaskCeleryOption(
        name='beat_sync_every', env_var='YTDL_CELERY_BEAT_SYNC_EVERY',
        type=int
    ),
    FlaskCeleryOption(
        name='beat_max_loop_interval',
        env_var='YTDL_CELERY_BEAT_MAX_LOOP_INTERVAL', type=int
    )
)
"""List of Celery env-var options that will be added to
`config.Config.celery_config`"""
