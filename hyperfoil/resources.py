from hyperfoil.defaults import DefaultResource, DefaultClient


class Benchmark(DefaultResource):

    def __init__(self, client: DefaultClient = None, entity: dict = None, content_type: str = '',
                 entity_id: str = "") -> None:
        super().__init__(client, entity, content_type, entity_id)

    def start(self):
        return self.client.start(self._entity_id)


class Run(DefaultResource):
    def __init__(self, client: DefaultClient = None, entity: dict = None, content_type: str = '',
                 entity_id: str = "") -> None:
        super().__init__(client, entity, content_type, entity_id)

    def kill(self):
        return self.client.kill(self._entity_id)

    def sessions(self):
        return self.client.sessions(self._entity_id)

    def recent_sessions(self):
        return self.client.recent_sessions(self._entity_id)

    def total_sessions(self):
        return self.client.total_sessions(self._entity_id)

    def connections(self):
        return self.client.connections(self._entity_id)
