

def test_create(benchmark, benchmark_yaml):
    assert benchmark.create(params=benchmark_yaml)
    mark = benchmark.read(benchmark_yaml['name'])
    assert mark.entity == benchmark_yaml


def test_all(benchmark, benchmark_yaml):
    assert benchmark.create(params=benchmark_yaml)
    all_benchmarks = benchmark.all()
    filtered = list(filter(lambda x: x.get('name') == benchmark_yaml['name'], all_benchmarks))
    assert len(filtered) == 1
    assert filtered[0].entity == benchmark_yaml
