from hyperfoil.defaults import DefaultResource, DefaultClient


class Benchmark(DefaultResource):

    def __init__(self, client: DefaultClient = None, entity: dict = None, content_type: str = '',
                 entity_id: str = "") -> None:
        super().__init__(client, entity, content_type, entity_id)
