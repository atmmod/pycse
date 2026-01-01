OK_FORMAT = True

name = "ex2b"
points = 6

from otter.test_files import test_case
import matplotlib.pyplot as plt
import numpy as np

@test_case(points=6, hidden=False)
def test_plotting(env):
    """Test that plot was created correctly"""
    # Get current figure and axes
    fig = plt.gcf()
    axes = plt.gca()

    assert len(fig.get_axes()) > 0, "No plot was created. Make sure to create a plot."

    # Check for axis labels
    xlabel = axes.get_xlabel()
    ylabel = axes.get_ylabel()
    assert xlabel != '', "X-axis label is missing. Add a label to the x-axis."
    assert ylabel != '', "Y-axis label is missing. Add a label to the y-axis."

    # Check for title
    title = axes.get_title()
    assert title != '', "Plot title is missing. Add a title to your plot."

    # Check that there's data plotted
    lines = axes.get_lines()
    assert len(lines) > 0, "No data plotted. Make sure you plot the energy vs temperature."

    # Verify the data makes sense (for 1000g Al, Cp=0.897)
    if len(lines) > 0:
        line = lines[0]
        xdata = line.get_xdata()
        ydata = line.get_ydata()

        assert len(xdata) > 5, "Plot should have multiple data points"
        assert len(ydata) > 5, "Plot should have multiple data points"

        # Check that energy increases with temperature
        assert np.all(np.diff(ydata) >= 0), "Energy should increase with temperature"

        # Rough check: at 500°C, ΔT = 475, q = 1000 * 0.897 * 475 = 426,075 J = 426.075 kJ
        max_energy = np.max(ydata)
        assert max_energy > 300, f"Maximum energy seems too low: {max_energy} kJ"
        assert max_energy < 600, f"Maximum energy seems too high: {max_energy} kJ"
