from typing import List

from hyperfoil.defaults import DefaultClient, DefaultResource
from hyperfoil.resources import Run, Benchmark


class BenchmarkClient(DefaultClient):
    def __init__(self, parent=None, instance_klass=None):
        super().__init__(parent, instance_klass=instance_klass)

    @property
    def url(self):
        return self.hyperfoil_client.url + '/benchmark'

    def list(self, **kwargs) -> List[DefaultResource]:
        response = self.rest.get(url=self.url, **kwargs)
        return [self._instance_klass(self, entity_id=name) for name in response.json()]

    def create(self, params: dict = None, **kwargs):
        response = self.rest.post(url=self.url, json=params, **kwargs)
        return response.ok

    def read(self, name: str) -> Benchmark:
        return self._instance_klass(client=self, entity_id=name)

    def start(self, name: str, **kwargs):
        url = self.url + f"/{name}/start"
        response = self.rest.get(url=url, **kwargs)
        return self._create_instance(response, klass=Run, client=self.parent.run)


class RunClient(DefaultClient):
    def __init__(self, parent=None, instance_klass=None) -> None:
        super().__init__(parent, instance_klass)

    @property
    def url(self):
        return self.hyperfoil_client.url + '/run'

    def list(self, **kwargs) -> List[DefaultResource]:
        response = self.rest.get(url=self.url, **kwargs)
        return [self._instance_klass(self, entity_id=name) for name in response.json()]

    def read(self, run_id: str) -> Run:
        return self._instance_klass(client=self, entity_id=run_id)

    def kill(self, run_id: str, **kwargs) -> bool:
        url = self._entity_url(run_id) + '/kill'
        response = self.rest.get(url=url, **kwargs)
        return response.ok

    def sessions(self, run_id: str, **kwargs) -> str:
        url = self._entity_url(run_id) + '/sessions'
        response = self.rest.get(url=url, **kwargs)
        # TODO: add test with run that takes longer time
        return response.content

    def recent_sessions(self, run_id: str, **kwargs):
        url = self._entity_url(run_id) + "/sessions/recent"
        response = self.rest.get(url=url, **kwargs)
        return response.json()

    def total_sessions(self, run_id: str, **kwargs) -> dict:
        url = self._entity_url(run_id) + '/sessions/total'
        response = self.rest.get(url=url, **kwargs)
        return response.json()

    def connections(self, run_id: str, **kwargs) -> str:
        url = self._entity_url(run_id) + '/connections'
        response = self.rest.get(url=url, **kwargs)
        return response.content.decode('utf-8')

    def all_stats(self, run_id: str, **kwargs) -> dict:
        headers = {'Accept': 'application/json'}
        url = self._entity_url(run_id) + '/stats/all'
        response = self.rest.get(url=url, headers=headers, **kwargs)
        return response.json()
