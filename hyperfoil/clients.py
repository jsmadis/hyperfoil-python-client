from hyperfoil.defaults import DefaultClient


class BenchmarkClient(DefaultClient):
    def __init__(self, parent=None, instance_klass=None):
        super().__init__(parent, instance_klass=instance_klass)

    @property
    def url(self):
        return self.url + '/benchmark'

    def all(self, **kwargs):
        response = self.rest.get(url=self.url, **kwargs)
        # TODO: Create list of benchmarks resources
        # TODO: Process response
        return response

    def create(self, params: dict = None, **kwargs):
        response = self.rest.post(url=self.url, json=params, **kwargs)
        # TODO: Process response
        return response

    def read(self, name: str, **kwargs):
        url = self.url + f"/{name}"
        response = self.rest.get(url=url, **kwargs)
        return self._create_instance(response)
