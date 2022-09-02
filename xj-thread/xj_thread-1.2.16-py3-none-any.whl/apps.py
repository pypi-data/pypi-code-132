from django.apps import AppConfig


class ThreadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'xj_thread'
    verbose_name = '发布系统'
    sort = 2
