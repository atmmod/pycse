test = {
    "name": "ex1a",
    "points": 10,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Test that arrays are defined
                    >>> import numpy as np
                    >>> assert 'x' in dir(), "x array not defined"
                    >>> assert 'deltaT' in dir(), "deltaT array not defined"
                    >>> assert isinstance(x, np.ndarray), "x should be a numpy array"
                    >>> assert isinstance(deltaT, np.ndarray), "deltaT should be a numpy array"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test array lengths
                    >>> assert len(x) == 6, "x should have 6 elements"
                    >>> assert len(deltaT) == 6, "deltaT should have 6 elements"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test Q_total_trapz calculation
                    >>> assert 'Q_total_trapz' in dir(), "Q_total_trapz not defined"
                    >>> assert isinstance(Q_total_trapz, (int, float, np.number)), "Q_total_trapz should be a number"
                    >>> assert 1100 < Q_total_trapz < 1300, f"Q_total_trapz value {Q_total_trapz} seems incorrect (expected ~1200 W)"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test exact value
                    >>> import numpy as np
                    >>> expected = 1201.106  # Calculated value
                    >>> assert abs(Q_total_trapz - expected) < 1.0, f"Q_total_trapz = {Q_total_trapz}, expected {expected}"
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
