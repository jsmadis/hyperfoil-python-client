from hyperfoil.defaults import DefaultClient


class BenchmarkClient(DefaultClient):
    def __init__(self, parent=None, instance_klass=None):
        super().__init__(parent, instance_klass=instance_klass)

    @property
    def url(self):
        return self.hyperfoil_client.url + '/benchmark'

    def all(self, **kwargs):
        response = self.rest.get(url=self.url, **kwargs)
        # TODO: Create list of benchmarks resources
        # TODO: Process response
        return response

    def create(self, params: dict = None, **kwargs):
        response = self.rest.post(url=self.url, json=params, **kwargs)
        return response.ok

    def read(self, name: str, **kwargs):
        return self._instance_klass(client=self, entity_id=name)
