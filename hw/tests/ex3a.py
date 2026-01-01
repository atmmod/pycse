OK_FORMAT = True

name = "ex3a"
points = 12

from otter.test_files import test_case
import numpy as np

@test_case(points=4, hidden=False)
def test_function_exists(env):
    """Check if dilution function exists"""
    possible_names = ['dilution_calculator', 'calculate_dilution', 'dilute', 'dilution']
    func_found = False
    for name in possible_names:
        if name in env:
            func_found = True
            break

    assert func_found, \
        "Dilution function not found. Expected one of: " + ", ".join(possible_names)

@test_case(points=4, hidden=False)
def test_calculate_c2(env):
    """Calculate C2 when C1, V1, V2 are known"""
    # C1=0.5 M, V1=100 mL, V2=250 mL -> C2 = C1*V1/V2 = 0.5*100/250 = 0.2 M
    possible_names = ['dilution_calculator', 'calculate_dilution', 'dilute', 'dilution']
    dilution_func = None
    for name in possible_names:
        if name in env:
            dilution_func = env[name]
            break

    try:
        result = dilution_func(C1=0.5, V1=100, V2=250, C2=None)
    except TypeError:
        result = dilution_func(0.5, 100, None, 250)

    assert result is not None, "Function should return a value"
    assert abs(result - 0.2) < 0.01, f"Test 1: Expected C2 ≈ 0.2 M, got {result}"

@test_case(points=4, hidden=False)
def test_calculate_v1(env):
    """Calculate V1 when C1, C2, V2 are known"""
    # C1=2.0 M, C2=0.1 M, V2=500 mL -> V1 = C2*V2/C1 = 0.1*500/2.0 = 25 mL
    possible_names = ['dilution_calculator', 'calculate_dilution', 'dilute', 'dilution']
    dilution_func = None
    for name in possible_names:
        if name in env:
            dilution_func = env[name]
            break

    try:
        result2 = dilution_func(C1=2.0, V1=None, C2=0.1, V2=500)
    except TypeError:
        result2 = dilution_func(2.0, None, 0.1, 500)

    assert result2 is not None, "Function should return a value"
    assert abs(result2 - 25) < 0.5, f"Test 2: Expected V1 ≈ 25 mL, got {result2}"
