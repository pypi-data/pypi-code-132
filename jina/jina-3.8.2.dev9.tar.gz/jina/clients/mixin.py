import time
import warnings
from functools import partialmethod
from typing import TYPE_CHECKING, AsyncGenerator, Dict, List, Optional, Union

from jina.helper import get_or_reuse_loop, run_async
from jina.importer import ImportExtensions

if TYPE_CHECKING:
    from docarray import DocumentArray

    from jina.clients.base import CallbackFnType, InputType
    from jina.types.request.data import Response


def _include_results_field_in_param(parameters: Optional['Dict']) -> 'Dict':
    key_result = '__results__'

    if parameters:

        if key_result in parameters:
            if not isinstance(parameters[key_result], dict):
                warnings.warn(
                    f'It looks like you passed a dictionary with the key `{key_result}` to `parameters`.'
                    'This key is reserved, so the associated value will be deleted.'
                )
                parameters.update({key_result: dict()})
    else:
        parameters = {key_result: dict()}

    return parameters


class MutateMixin:
    """The GraphQL Mutation Mixin for Client and Flow"""

    def mutate(
        self,
        mutation: str,
        variables: Optional[dict] = None,
        timeout: Optional[float] = None,
        headers: Optional[dict] = None,
    ):
        """Perform a GraphQL mutation

        :param mutation: the GraphQL mutation as a single string.
        :param variables: variables to be substituted in the mutation. Not needed if no variables are present in the mutation string.
        :param timeout: HTTP request timeout
        :param headers: HTTP headers
        :return: dict containing the optional keys ``data`` and ``errors``, for response data and errors.
        """
        with ImportExtensions(required=True):
            from sgqlc.endpoint.http import HTTPEndpoint as SgqlcHTTPEndpoint

            proto = 'https' if self.args.tls else 'http'
            graphql_url = f'{proto}://{self.args.host}:{self.args.port}/graphql'
            endpoint = SgqlcHTTPEndpoint(graphql_url)
            res = endpoint(
                mutation, variables=variables, timeout=timeout, extra_headers=headers
            )
            if 'errors' in res and res['errors']:
                msg = 'GraphQL mutation returned the following errors: '
                for err in res['errors']:
                    msg += err['message'] + '. '
                raise ConnectionError(msg)
            return res


class AsyncMutateMixin(MutateMixin):
    """The async GraphQL Mutation Mixin for Client and Flow"""

    async def mutate(
        self,
        mutation: str,
        variables: Optional[dict] = None,
        timeout: Optional[float] = None,
        headers: Optional[dict] = None,
    ):
        """Perform a GraphQL mutation, asynchronously

        :param mutation: the GraphQL mutation as a single string.
        :param variables: variables to be substituted in the mutation. Not needed if no variables are present in the mutation string.
        :param timeout: HTTP request timeout
        :param headers: HTTP headers
        :return: dict containing the optional keys ``data`` and ``errors``, for response data and errors.
        """
        return await get_or_reuse_loop().run_in_executor(
            None, super().mutate, mutation, variables, timeout, headers
        )


class HealthCheckMixin:
    """The Health check Mixin for Client and Flow to expose `dry_run` API"""

    def dry_run(self, **kwargs) -> bool:
        """Sends a dry run to the Flow to validate if the Flow is ready to receive requests

        :param kwargs: potential kwargs received passed from the public interface
        :return: boolean indicating the health/readiness of the Flow
        """
        return run_async(self.client._dry_run, **kwargs)


class AsyncHealthCheckMixin:
    """The Health check Mixin for Client and Flow to expose `dry_run` API"""

    async def dry_run(self, **kwargs) -> bool:
        """Sends a dry run to the Flow to validate if the Flow is ready to receive requests

        :param kwargs: potential kwargs received passed from the public interface
        :return: boolean indicating the health/readiness of the Flow
        """
        return await self.client._dry_run(**kwargs)


def _render_response_table(r, st, ed, show_table: bool = True):

    from rich import print

    elapsed = (ed - st) * 1000
    route = r.routes
    gateway_time = (
        route[0].end_time.ToMilliseconds() - route[0].start_time.ToMilliseconds()
    )
    exec_time = {}

    if len(route) > 1:
        for r in route[1:]:
            exec_time[r.executor] = (
                r.end_time.ToMilliseconds() - r.start_time.ToMilliseconds()
            )
    network_time = elapsed - gateway_time
    server_network = gateway_time - sum(exec_time.values())
    from rich.table import Table

    def make_table(_title, _time, _percent):
        table = Table(show_header=False, box=None)
        table.add_row(
            _title, f'[b]{_time:.0f}[/b]ms', f'[dim]{_percent * 100:.0f}%[/dim]'
        )
        return table

    from rich.tree import Tree

    t = Tree(make_table('Roundtrip', elapsed, 1))
    t.add(make_table('Client-server network', network_time, network_time / elapsed))
    t2 = t.add(make_table('Server', gateway_time, gateway_time / elapsed))
    t2.add(
        make_table(
            'Gateway-executors network', server_network, server_network / gateway_time
        )
    )
    for _name, _time in exec_time.items():
        t2.add(make_table(_name, _time, _time / gateway_time))

    if show_table:
        print(t)
    return {
        'Roundtrip': elapsed,
        'Client-server network': network_time,
        'Server': gateway_time,
        'Gateway-executors network': server_network,
        **exec_time,
    }


class ProfileMixin:
    """The Profile Mixin for Client and Flow to expose `profile` API"""

    def profiling(self, show_table: bool = True) -> Dict[str, float]:
        """Profiling a single query's roundtrip including network and computation latency. Results is summarized in a Dict.

        :param show_table: whether to show the table or not.
        :return: the latency report in a dict.
        """
        from jina import Document

        st = time.perf_counter()
        r = self.client.post('/', Document, return_responses=True)
        ed = time.perf_counter()
        return _render_response_table(r[0], st, ed, show_table=show_table)


class AsyncProfileMixin:
    """The Profile Mixin for Client and Flow to expose `profile` API"""

    async def profiling(self, show_table: bool = True) -> Dict[str, float]:
        """Profiling a single query's roundtrip including network and computation latency. Results is summarized in a Dict.

        :param show_table: whether to show the table or not.
        :return: the latency report in a dict.
        """
        from jina import Document

        st = time.perf_counter()
        async for r in self.client.post('/', Document, return_responses=True):
            ed = time.perf_counter()
            return _render_response_table(r, st, ed, show_table=show_table)


class PostMixin:
    """The Post Mixin class for Client and Flow"""

    def post(
        self,
        on: str,
        inputs: Optional['InputType'] = None,
        on_done: Optional['CallbackFnType'] = None,
        on_error: Optional['CallbackFnType'] = None,
        on_always: Optional['CallbackFnType'] = None,
        parameters: Optional[Dict] = None,
        target_executor: Optional[str] = None,
        request_size: int = 100,
        show_progress: bool = False,
        continue_on_error: bool = False,
        return_responses: bool = False,
        **kwargs,
    ) -> Optional[Union['DocumentArray', List['Response']]]:
        """Post a general data request to the Flow.

        :param inputs: input data which can be an Iterable, a function which returns an Iterable, or a single Document.
        :param on: the endpoint which is invoked. All the functions in the executors decorated by `@requests(on=...)` with the same endpoint are invoked.
        :param on_done: the function to be called when the :class:`Request` object is resolved.
        :param on_error: the function to be called when the :class:`Request` object is rejected.
        :param on_always: the function to be called when the :class:`Request` object is either resolved or rejected.
        :param parameters: the kwargs that will be sent to the executor
        :param target_executor: a regex string. Only matching Executors will process the request.
        :param request_size: the number of Documents per request. <=0 means all inputs in one request.
        :param show_progress: if set, client will show a progress bar on receiving every request.
        :param continue_on_error: if set, a Request that causes callback error will be logged only without blocking the further requests.7
        :param return_responses: if set to True, the result will come as Response and not as a `DocumentArray`

        :param kwargs: additional parameters
        :return: None or DocumentArray containing all response Documents

        .. warning::
            ``target_executor`` uses ``re.match`` for checking if the pattern is matched. ``target_executor=='foo'`` will match both deployments with the name ``foo`` and ``foo_what_ever_suffix``.
        """

        c = self.client
        c.show_progress = show_progress
        c.continue_on_error = continue_on_error

        parameters = _include_results_field_in_param(parameters)

        from jina import DocumentArray

        return_results = (on_always is None) and (on_done is None)

        async def _get_results(*args, **kwargs):
            result = [] if return_responses else DocumentArray()
            async for resp in c._get_results(*args, **kwargs):
                if return_results:
                    if return_responses:
                        result.append(resp)
                    else:
                        result.extend(resp.data.docs)
            if return_results:
                return result

        return run_async(
            _get_results,
            inputs=inputs,
            on_done=on_done,
            on_error=on_error,
            on_always=on_always,
            exec_endpoint=on,
            target_executor=target_executor,
            parameters=parameters,
            request_size=request_size,
            **kwargs,
        )

    # ONLY CRUD, for other request please use `.post`
    index = partialmethod(post, '/index')
    search = partialmethod(post, '/search')
    update = partialmethod(post, '/update')
    delete = partialmethod(post, '/delete')


class AsyncPostMixin:
    """The Async Post Mixin class for AsyncClient and AsyncFlow"""

    async def post(
        self,
        on: str,
        inputs: Optional['InputType'] = None,
        on_done: Optional['CallbackFnType'] = None,
        on_error: Optional['CallbackFnType'] = None,
        on_always: Optional['CallbackFnType'] = None,
        parameters: Optional[Dict] = None,
        target_executor: Optional[str] = None,
        request_size: int = 100,
        show_progress: bool = False,
        continue_on_error: bool = False,
        return_responses: bool = False,
        **kwargs,
    ) -> AsyncGenerator[None, Union['DocumentArray', 'Response']]:
        """Async Post a general data request to the Flow.

        :param inputs: input data which can be an Iterable, a function which returns an Iterable, or a single Document.
        :param on: the endpoint which is invoked. All the functions in the executors decorated by `@requests(on=...)` with the same endpoint are invoked.
        :param on_done: the function to be called when the :class:`Request` object is resolved.
        :param on_error: the function to be called when the :class:`Request` object is rejected.
        :param on_always: the function to be called when the :class:`Request` object is either resolved or rejected.
        :param parameters: the kwargs that will be sent to the executor
        :param target_executor: a regex string. Only matching Executors will process the request.
        :param request_size: the number of Documents per request. <=0 means all inputs in one request.
        :param show_progress: if set, client will show a progress bar on receiving every request.
        :param continue_on_error: if set, a Request that causes callback error will be logged only without blocking the further requests.
        :param return_responses: if set to True, the result will come as Response and not as a `DocumentArray`
        :param kwargs: additional parameters, can be used to pass metadata or authentication information in the server call
        :yield: Response object

        .. warning::
            ``target_executor`` uses ``re.match`` for checking if the pattern is matched. ``target_executor=='foo'`` will match both deployments with the name ``foo`` and ``foo_what_ever_suffix``.
        """
        c = self.client
        c.show_progress = show_progress
        c.continue_on_error = continue_on_error

        parameters = _include_results_field_in_param(parameters)

        async for result in c._get_results(
            inputs=inputs,
            on_done=on_done,
            on_error=on_error,
            on_always=on_always,
            exec_endpoint=on,
            target_executor=target_executor,
            parameters=parameters,
            request_size=request_size,
            **kwargs,
        ):
            if not return_responses:
                yield result.data.docs
            else:
                yield result

    # ONLY CRUD, for other request please use `.post`
    index = partialmethod(post, '/index')
    search = partialmethod(post, '/search')
    update = partialmethod(post, '/update')
    delete = partialmethod(post, '/delete')
