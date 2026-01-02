test = {
    "name": "ex1b",
    "points": 8,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Test that Q_cumulative is defined
                    >>> assert 'Q_cumulative' in dir(), "Q_cumulative not defined"
                    >>> import numpy as np
                    >>> assert isinstance(Q_cumulative, np.ndarray), "Q_cumulative should be a numpy array"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test Q_cumulative length
                    >>> assert len(Q_cumulative) == 6, f"Q_cumulative should have 6 elements, got {len(Q_cumulative)}"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test that cumulative values are increasing
                    >>> import numpy as np
                    >>> diffs = np.diff(Q_cumulative)
                    >>> assert all(diffs >= 0), "Cumulative heat should be monotonically increasing"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test specific value at index 3 (6 m position)
                    >>> expected_at_6m = 721.0  # Approximate value
                    >>> assert abs(Q_cumulative[3] - expected_at_6m) < 10, f"Value at 6m should be ~{expected_at_6m}, got {Q_cumulative[3]}"
                    """,
                    "hidden": True,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test that final value matches total from part A
                    >>> assert abs(Q_cumulative[-1] - Q_total_trapz) < 0.1, "Final cumulative value should equal total from Part A"
                    """,
                    "hidden": True,
                    "locked": False
                }
            ],
            "scored": True,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}
