from typing import List

from hyperfoil.defaults import DefaultClient, DefaultResource


class BenchmarkClient(DefaultClient):
    def __init__(self, parent=None, instance_klass=None):
        super().__init__(parent, instance_klass=instance_klass)

    @property
    def url(self):
        return self.hyperfoil_client.url + '/benchmark'

    def all(self, **kwargs) -> List[DefaultResource]:
        response = self.rest.get(url=self.url, **kwargs)
        return [self._instance_klass(self, entity_id=name) for name in response.json()]

    def create(self, params: dict = None, **kwargs):
        response = self.rest.post(url=self.url, json=params, **kwargs)
        return response.ok

    def read(self, name: str, **kwargs):
        return self._instance_klass(client=self, entity_id=name)


class RunClient(DefaultClient):
    def __init__(self, parent=None, instance_klass=None) -> None:
        super().__init__(parent, instance_klass)

    @property
    def url(self):
        return self.hyperfoil_client.url + '/run'

    def all(self, **kwargs) -> List[DefaultResource]:
        response = self.rest.get(url=self.url, **kwargs)
        return [self._instance_klass(self, entity_id=name) for name in response.json()]

    def read(self, run_id: str):
        return self._instance_klass(client=self, entity_id=run_id)
