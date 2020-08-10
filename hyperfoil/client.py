from urllib.parse import urljoin

import requests

from hyperfoil import resources
from hyperfoil.clients import BenchmarkClient



class HyperfoilClient:
    def __init__(self, url: str) -> None:
        self._rest = RestApiClient(url)
        self._benchmark = BenchmarkClient(self, instance_klass=resources.Benchmark)

    @property
    def hyperfoil_client(self) -> 'HyperfoilClient':
        return self

    @property
    def rest(self) -> 'RestApiClient':
        return self._rest

    @property
    def benchmark(self) -> 'BenchmarkClient':
        return self._benchmark


class RestApiClient:
    def __init__(self, url: str, verify_ssl=False):
        self._url = url
        self._verify_ssl = verify_ssl

    @property
    def url(self) -> str:
        return self._url

    def request(self, method='GET', url=None, path='', params: dict = None,
                headers: dict = None, **kwargs):
        full_url = url if url else urljoin(self._url, path)
        headers = headers or {}
        params = params or {}
        response = requests.request(method=method, url=full_url, headers=headers,
                                    params=params, verify=self._verify_ssl, **kwargs)
        # TODO: add response processing
        return response

    def get(self, *args, **kwargs):
        return self.request('GET', *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.request('POST', *args, **kwargs)
