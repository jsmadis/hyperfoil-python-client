from time import sleep

import pytest


@pytest.fixture(autouse=True)
def create_benchmark(benchmark_yaml, benchmark):
    assert benchmark.create(params=benchmark_yaml)
    return benchmark_yaml['name']


@pytest.fixture(scope='module')
def finished_benchmark(benchmark_yaml, benchmark):
    assert benchmark.create(params=benchmark_yaml)
    run_resource = benchmark.start(benchmark_yaml['name'])
    assert run_resource
    sleep(60)
    return run_resource


def test_all_runs(run):
    assert run.list()


def test_get_run_by_id(finished_benchmark, create_benchmark, run):
    run_read = run.read(run_id=finished_benchmark['id'])
    assert run_read
    assert run_read.get('id') == finished_benchmark['id']
    assert run_read.get('benchmark') == create_benchmark
    assert run_read.get('errors') == []


def test_kill_run(benchmark, create_benchmark, run):
    run_resource = benchmark.start(create_benchmark)
    assert run_resource
    killed = run.kill(run_resource['id'])
    assert killed
    run_read = run.read(run_resource['id'])
    assert run_read
    assert run_read.get('id') == run_resource['id']
    assert bool(run_read.get('cancelled'))


def test_recent_sessions(finished_benchmark, create_benchmark, run):
    #TODO: add long running benchmark so we can check recent session
    recent_sessions = run.recent_sessions(finished_benchmark['id'])
    assert recent_sessions == {}


def test_total_sessions(finished_benchmark, create_benchmark, run):
    # TODO: add long running benchmark so we can check total sessions
    total_sessions = run.total_sessions(finished_benchmark['id'])
    assert total_sessions == {}


def test_benchmark_resource_start(benchmark, create_benchmark, run):
    mark = benchmark.read(create_benchmark)
    run_resource = mark.start()
    assert run_resource
    run_read = run.read(run_id=run_resource['id'])
    assert run_read
    assert run_read.get('id') == run_resource['id']


def test_run_connections(finished_benchmark, create_benchmark, run):
    # TODO add long running test
    connections = run.connections(finished_benchmark['id'])
    assert connections == ''


def test_all_stats(finished_benchmark, create_benchmark, run):
    # TODO add long running test
    stats = run.all_stats(finished_benchmark['id'])
    assert stats
    assert stats['info']['id'] == finished_benchmark['id']
    assert stats['info']['benchmark'] == create_benchmark
