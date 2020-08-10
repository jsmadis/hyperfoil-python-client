from urllib.parse import urljoin

import requests


class HyperfoilClient:
    def __init__(self, url: str) -> None:
        self._rest = RestApiClient(url)


class RestApiClient:
    def __init__(self, url: str, verify_ssl=False):
        self._url = url
        self._verify_ssl = verify_ssl

    def request(self, method='GET', url=None, path='', params:dict = None,
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
