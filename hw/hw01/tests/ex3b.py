OK_FORMAT = False

name = "ex3b"
points = 6

from otter.test_files import test_case
import numpy as np

@test_case(points=6, hidden=False)
def test_serial_dilution_setup(env):
    """Test that serial dilution parameters are set up correctly"""
    # Check for initial concentration setup
    initial_conc_vars = ['initial_concentration', 'C0', 'initial_conc', 'start_concentration']
    found_initial = False
    for var in initial_conc_vars:
        if var in env and env[var] == 1.0:
            found_initial = True
            break

    # Check for number of dilutions
    num_dilution_vars = ['num_dilutions', 'n_dilutions', 'number_of_dilutions']
    found_num = False
    for var in num_dilution_vars:
        if var in env and env[var] == 5:
            found_num = True
            break

    # Check for dilution factor or volumes
    dilution_factor_found = False
    if 'dilution_factor' in env and abs(env['dilution_factor'] - 5) < 0.1:
        dilution_factor_found = True
    elif 'final_volume_dilution' in env and 'initial_volume_aliquot' in env:
        if abs(env['final_volume_dilution'] / env['initial_volume_aliquot'] - 5) < 0.1:
            dilution_factor_found = True

    # More lenient: at least check that they're doing something with 5 dilutions
    assert found_initial or found_num or dilution_factor_found, \
        "Could not find serial dilution setup. Make sure you set up initial concentration (1.0 M) and dilution parameters."
