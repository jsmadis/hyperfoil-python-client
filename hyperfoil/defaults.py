from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hyperfoil.client import HyperfoilClient, RestApiClient


class DefaultClient:
    def __init__(self, parent=None) -> None:
        self._parent = parent

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


class DefaultResource:
    def __init__(self) -> None:
        super().__init__()
