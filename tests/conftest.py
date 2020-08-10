import os

import pytest
from dotenv import load_dotenv

from hyperfoil import HyperfoilClient


load_dotenv()


@pytest.fixture(scope='session')
def url() -> str:
    return os.getenv('HYPERFOIL_URL')


@pytest.fixture(scope='session')
def client(url) -> HyperfoilClient:
    return HyperfoilClient(url)


@pytest.fixture(scope='session')
def benchmark(client):
    return client.benchmark
