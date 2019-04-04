import pytest

def pytest_addoption(parser):
    parser.addoption("--seed", type=int, help="random generator seed")

@pytest.fixture
def seedval():
    import numpy as np
    seedval = pytest.config.getoption('seed')
    if seedval is None:
        seedval = np.random.randint(2**32)
    return seedval
