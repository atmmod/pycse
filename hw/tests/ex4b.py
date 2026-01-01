OK_FORMAT = True

name = "ex4b"
points = 8

from otter.test_files import test_case
import matplotlib.pyplot as plt
import numpy as np

@test_case(points=8, hidden=False)
def test_reaction_rate_plotting(env):
    """Test that plot was created correctly with 3 curves"""
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

    # Check for legend (since plotting 3 curves)
    legend = axes.get_legend()
    assert legend is not None, "Legend is missing. Add a legend to distinguish the three rate constants."

    # Check that multiple lines are plotted (should be 3)
    lines = axes.get_lines()
    assert len(lines) >= 3, f"Expected 3 lines (for 3 different k values), found {len(lines)}"

    # Verify the data makes sense
    for i, line in enumerate(lines[:3]):
        xdata = line.get_xdata()
        ydata = line.get_ydata()

        # Check that we have data
        assert len(xdata) > 5, f"Line {i+1} should have multiple data points"

        # Check that concentration decreases over time
        assert ydata[0] > ydata[-1], f"Line {i+1}: Concentration should decrease over time"

        # Check starting value is close to C0 = 2.0
        assert abs(ydata[0] - 2.0) < 0.1, f"Line {i+1}: Should start at C0 ≈ 2.0 M, got {ydata[0]}"

        # Check that concentration is always positive
        assert np.all(ydata > 0), f"Line {i+1}: Concentration should always be positive"
