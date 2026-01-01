OK_FORMAT = True

name = "ex1b"
points = 6

from otter.test_files import test_case
import numpy as np

@test_case(points=6, hidden=False)
def test_array_operations(env):
    """Test temperature array and pressure calculations"""
    # Expected temperatures from 250 to 400 in steps of 25
    temps = np.arange(250, 401, 25)

    # Students should have created temperature array
    temp_vars = ['temps', 'temperatures', 'T_array', 'temp_array']
    found_temps = False
    for var in temp_vars:
        if var in env:
            found_temps = True
            break

    assert found_temps, "Temperature array not found. Make sure to create an array of temperatures."

    # Check for pressure calculations
    pressure_vars = ['pressures', 'P_array', 'pressure_array']
    found_pressures = False
    student_pressures = None

    for var in pressure_vars:
        if var in env:
            student_pressures = env[var]
            found_pressures = True
            break

    if not found_pressures:
        # Look for any array with the right size
        for key, val in env.items():
            if isinstance(val, np.ndarray) and len(val) == 7:
                student_pressures = val
                found_pressures = True
                break

    assert found_pressures, "Could not find pressure array. Did you store the results?"
    assert len(student_pressures) == 7, f"Expected 7 pressure values, got {len(student_pressures)}"
