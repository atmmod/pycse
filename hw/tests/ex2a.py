OK_FORMAT = False

name = "ex2a"
points = 12

from otter.test_files import test_case
import numpy as np

@test_case(points=4, hidden=False)
def test_function_exists(env):
    """Check if calculate_heat function exists"""
    assert 'calculate_heat' in env, "Function calculate_heat is not defined"

@test_case(points=4, hidden=False)
def test_water_heating(env):
    """Test water heating calculation (500g, Cp=4.184, 20°C to 100°C)"""
    # q = m * Cp * ΔT = 500 * 4.184 * 80 = 167,360 J = 167.36 kJ
    result = env['calculate_heat'](500, 4.184, 20, 100)

    if result is not None:
        if isinstance(result, tuple):
            q_j, q_kj = result
            assert abs(q_j - 167360) < 10, f"Expected ~167360 J, got {q_j} J"
            assert abs(q_kj - 167.36) < 0.1, f"Expected ~167.36 kJ, got {q_kj} kJ"
        else:
            # Single return value
            assert abs(result - 167360) < 10 or abs(result - 167.36) < 0.1, \
                f"Expected energy of ~167360 J or ~167.36 kJ, got {result}"

@test_case(points=4, hidden=False)
def test_simple_case(env):
    """Test simple calculation"""
    result2 = env['calculate_heat'](100, 1.0, 0, 10)
    # q = 100 * 1.0 * 10 = 1000 J = 1 kJ
    if result2 is not None:
        if isinstance(result2, tuple):
            assert abs(result2[0] - 1000) < 1, "Simple calculation check failed"
        else:
            assert abs(result2 - 1000) < 1 or abs(result2 - 1.0) < 0.01, "Simple calculation check failed"
