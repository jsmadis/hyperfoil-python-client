import collections
from typing import TYPE_CHECKING, Any, Iterator

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
        if 'text/vnd.yaml' in response.headers.get("Content-Type", ""):
            extracted = yaml.load(response.content.decode('utf-8'), Loader=yaml.Loader)
            return klass(client=self, entity=extracted, content_type='text/vnd.yaml') if klass else extracted

        return klass(client=self, entity=response.json(), content_type='application/json')


class DefaultResource(collections.abc.MutableMapping):
    def __init__(self, client: DefaultClient = None, entity: dict = None,
                 content_type: str = '') -> None:
        self._entity = entity
        self._client = client
        self._content_type = content_type

    @property
    def entity(self) -> dict:
        return self._entity

    def get(self, item):
        return self.entity.get(item)

    def set(self, item: str, value: Any):
        self.entity[item] = value

    def __getitem__(self, item: str):
        return self.entity.get(item)

    def __setitem__(self, key: str, value):
        self.set(key, value)

    def __delitem__(self, key: str):
        del self.entity[key]

    def __len__(self) -> int:
        return len(self.entity)

    def __iter__(self) -> Iterator:
        return iter(self.entity)
