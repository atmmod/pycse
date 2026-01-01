OK_FORMAT = False

name = "ex3b"
points = 6

from otter.test_files import test_case
import numpy as np

@test_case(points=6, hidden=False)
def test_serial_dilution(env):
    """Test serial dilution analysis"""
    # For serial dilution: Start with 10 mL of 1.0 M, dilute to 50 mL (5x dilution)
    # Dilution factor = 5 each time
    # After dilution 1: 1.0/5 = 0.2 M
    # After dilution 2: 0.2/5 = 0.04 M
    # After dilution 3: 0.04/5 = 0.008 M
    # After dilution 4: 0.008/5 = 0.0016 M
    # After dilution 5: 0.0016/5 = 0.00032 M

    expected_concentrations = np.array([0.2, 0.04, 0.008, 0.0016, 0.00032])

    # Look for concentration array with various possible names
    found = False
    concentration_vars = ['concentrations', 'conc', 'C', 'dilutions', 'serial_dilutions']

    for var_name in concentration_vars:
        if var_name in env:
            student_conc = env[var_name]
            if isinstance(student_conc, (list, np.ndarray)):
                student_conc = np.array(student_conc)
                if len(student_conc) == 5:
                    # Check if values match expected (with some tolerance)
                    relative_errors = np.abs((student_conc - expected_concentrations) / expected_concentrations)
                    if np.all(relative_errors < 0.05):  # Within 5% error
                        found = True
                        break

    if not found:
        # More lenient check - just verify the pattern exists
        for var_name in env.keys():
            var = env[var_name]
            if isinstance(var, (list, np.ndarray)):
                var = np.array(var)
                if len(var) == 5:
                    # Check if it's a decreasing sequence
                    if np.all(np.diff(var) < 0):
                        # Check if ratio between consecutive elements is ~5
                        ratios = var[:-1] / var[1:]
                        if np.all(np.abs(ratios - 5) < 0.5):
                            found = True
                            break

    assert found, "Could not find serial dilution concentrations. Make sure you create an array with 5 dilution concentrations."
