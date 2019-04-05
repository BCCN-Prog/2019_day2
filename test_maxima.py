import numpy as np
import pytest

from maxima import find_maxima

test_cases = [
([0, 1, 2, 1, 2, 1, 0], [2, 4]),
([-i**2 for i in range(-3, 4)], [3]),
([np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)], [16,78]),
([4, 2, 1, 3, 1, 2], [0, 3, 5]),
([4, 2, 1, 3, 1, 5], [0, 3, 5]),
([4, 2, 1, 3, 1], [0, 3]),
]

@pytest.mark.parametrize('inp, exp', test_cases)
def test_maxima(inp, exp):
    out = find_maxima(inp)
    assert out == exp
    impl_test(inp, out)


def test_randomized(seedval):
    # Given
    rand_gen = np.random.RandomState(seed=seedval)
    numel = rand_gen.randint(0, 1000)
    test_vec = rand_gen.randint(20, size=numel)

    # When
    out = find_maxima(test_vec)

    # Then
    impl_test(test_vec, out)


def impl_test(test_vec, out):
    print(f'test_vec: {test_vec}')
    print(f'out: {out}')

    dv = np.diff(out)
    assert np.all(dv > 1), "Adjacent local maxima is impossible"

    first = out[0]
    last = out[-1]

    if first == 0:
        assert test_vec[0] > test_vec[1]
        middle = out[1:-1]
    else:
        middle = out[:-1]

    if len(middle) > 1:
        for i, j in zip(middle[:-1], middle[1:]):
            up = False
            v1, v0 = test_vec[i], test_vec[i-1]
            assert v1 > v0, f'i: {i}, inp[i]: {v1}, inp[i-1]: {v0}'
            for k in range(i+1, j):
                v1, v0 = test_vec[k], test_vec[k-1]
                if v1 > v0:
                    up = True
                elif v1 < v0:
                    assert not up, f'i: {i}, j: {j}, k: {k}'
        assert test_vec[j] > test_vec[j-1], f'i: {i}, j: {j}'


    if last == len(test_vec) - 1:
        assert test_vec[-1] > test_vec[-2]
    else:
        for k in range(last+1, len(test_vec)):
            assert test_vec[k] <= test_vec[k-1], f'{k}'


