from typing import TYPE_CHECKING

import requests
import yaml

if TYPE_CHECKING:
    from hyperfoil.client import HyperfoilClient, RestApiClient


class DefaultClient:
    def __init__(self, parent=None, instance_klass=None) -> None:
        self._parent = parent
        self._instance_klass = instance_klass

    @property
    def hyperfoil_client(self) -> 'HyperfoilClient':
        return self.parent.hyperfoil_client

    @property
    def parent(self) -> 'HyperfoilClient':
        return self._parent

    @property
    def rest(self) -> 'RestApiClient':
        return self.parent.rest

    @property
    def url(self) -> str:
        return self.rest.url

    def _create_instance(self, response: requests.Response, klass=None):
        klass = klass or self._instance_klass
        if response.headers.get("Content-Type") == 'text/vnd.yaml':
            extracted = yaml.load(response.content.decode('utf-8'), Loader=yaml.Loader)
            instance = klass(client=self, entity=extracted, content_type='text/vnd.yaml') if klass else extracted
            return instance

        # TODO add json processing


class DefaultResource:
    def __init__(self, entity: dict = None, client: DefaultClient = None
                 , content_type: str = "") -> None:
        self._entity = entity
        self._client = client
        self._content_type = content_type
