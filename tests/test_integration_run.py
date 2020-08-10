import pytest


@pytest.fixture(autouse=True)
def create_benchmark(benchmark_yaml, benchmark):
    assert benchmark.create(params=benchmark_yaml)
    return benchmark_yaml['name']


def test_all_runs(run):
    assert run.list()


def test_get_run_by_id(benchmark, create_benchmark, run):
    run_resource = benchmark.start(create_benchmark)
    assert run_resource
    run_read = run.read(run_id=run_resource['id'])
    assert run_read
    assert run_read.get('id') == run_resource['id']
    assert run_read.get('benchmark') == create_benchmark
    assert run_read.get('errors') == []
