import pytest
import yaml


@pytest.fixture
def benchmark_yaml():
    with open('benchmarks/hello-world.yaml') as file:
        data = file.read()
    return yaml.load(data, Loader=yaml.Loader)


def test_create(benchmark, benchmark_yaml):
    assert benchmark.create(params=benchmark_yaml)
    mark = benchmark.read(benchmark_yaml['name'])
    assert mark.entity == benchmark_yaml
