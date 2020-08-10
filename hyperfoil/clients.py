from hyperfoil.defaults import DefaultClient


class BenchmarkClient(DefaultClient):
    def __init__(self, parent=None):
        super().__init__(parent)

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
