OK_FORMAT = True

name = "ex1a"
points = 12

from otter.test_files import test_case
import numpy as np

@test_case(points=4, hidden=False)
def test_function_exists(env):
    """Check if calculate_pressure function exists"""
    assert 'calculate_pressure' in env, "Function calculate_pressure is not defined"

@test_case(points=4, hidden=False)
def test_basic_calculation(env):
    """Test basic pressure calculation (PV = nRT)"""
    # For V=10.0, n=2.5, T=298.15, R=0.08206
    # P = nRT/V = 2.5 * 0.08206 * 298.15 / 10.0 = 6.112 atm
    result = env['calculate_pressure'](10.0, 2.5, 298.15)
    assert result is not None, "Function should return a value"
    assert isinstance(result, (int, float, np.number)), "Function should return a numeric value"
    assert abs(result - 6.112) < 0.01, f"Expected pressure ≈ 6.112 atm, got {result}"

@test_case(points=4, hidden=False)
def test_different_values(env):
    """Test with different input values"""
    result2 = env['calculate_pressure'](5.0, 1.0, 273.15)
    expected2 = 1.0 * 0.08206 * 273.15 / 5.0
    assert abs(result2 - expected2) < 0.01, f"Expected pressure ≈ {expected2} atm, got {result2}"
