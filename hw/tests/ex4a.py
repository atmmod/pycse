OK_FORMAT = True

name = "ex4a"
points = 10

from otter.test_files import test_case
import numpy as np

@test_case(points=3, hidden=False)
def test_function_exists(env):
    """Check if concentration function exists"""
    possible_names = ['concentration', 'calc_concentration', 'C_t', 'conc_time', 'concentration_time']
    func_found = False
    for name in possible_names:
        if name in env:
            func_found = True
            break

    assert func_found, \
        "Concentration function not found. Expected one of: " + ", ".join(possible_names)

@test_case(points=3, hidden=False)
def test_initial_concentration(env):
    """Verify calculation at t=0"""
    # C(0) = C0 * exp(-k*0) = C0
    possible_names = ['concentration', 'calc_concentration', 'C_t', 'conc_time', 'concentration_time']
    conc_func = None
    for name in possible_names:
        if name in env:
            conc_func = env[name]
            break

    try:
        result = conc_func(0, 2.0, 0.05)  # t, C0, k
    except TypeError:
        try:
            result = conc_func(2.0, 0.05, 0)  # C0, k, t
        except:
            result = conc_func(C0=2.0, k=0.05, t=0)

    assert abs(result - 2.0) < 0.01, f"At t=0, C should equal C0=2.0, got {result}"

@test_case(points=4, hidden=False)
def test_exponential_decay(env):
    """Verify exponential decay"""
    # C(t) = 2.0 * exp(-0.05 * 20) = 2.0 * exp(-1) ≈ 0.736
    possible_names = ['concentration', 'calc_concentration', 'C_t', 'conc_time', 'concentration_time']
    conc_func = None
    for name in possible_names:
        if name in env:
            conc_func = env[name]
            break

    try:
        result2 = conc_func(20, 2.0, 0.05)
    except TypeError:
        try:
            result2 = conc_func(2.0, 0.05, 20)
        except:
            result2 = conc_func(C0=2.0, k=0.05, t=20)

    expected = 2.0 * np.exp(-0.05 * 20)
    assert abs(result2 - expected) < 0.01, f"Expected C(20) ≈ {expected:.3f}, got {result2:.3f}"
