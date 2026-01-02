test = {
    "name": "ex4b",
    "points": 6,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Test that find_maximum function is defined
                    >>> assert 'find_maximum' in dir(), "find_maximum function not defined"
                    >>> assert callable(find_maximum), "find_maximum should be a function"
                    >>> assert hasattr(find_maximum, 'direction'), "find_maximum should have direction attribute"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test that oscillation_period is defined
                    >>> assert 'oscillation_period' in dir(), "oscillation_period not defined"
                    >>> assert isinstance(oscillation_period, (int, float, np.number)), "oscillation_period should be a number"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test oscillation_period is positive and reasonable
                    >>> assert oscillation_period > 0, "oscillation_period should be positive"
                    >>> assert oscillation_period < 20, f"oscillation_period = {oscillation_period} seems too large"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test oscillation_period value against theory
                    >>> import numpy as np
                    >>> omega_n = 0.5
                    >>> zeta = 0.2
                    >>> theoretical = 2 * np.pi / (omega_n * np.sqrt(1 - zeta**2))
                    >>> assert abs(oscillation_period - theoretical) < 0.5, f"oscillation_period = {oscillation_period} should be near theoretical {theoretical}"
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
