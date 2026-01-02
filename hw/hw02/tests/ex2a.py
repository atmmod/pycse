test = {
    "name": "ex2a",
    "points": 12,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Test that dCAdt function is defined
                    >>> assert 'dCAdt' in dir(), "dCAdt function not defined"
                    >>> assert callable(dCAdt), "dCAdt should be a function"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test that sol is defined
                    >>> assert 'sol' in dir(), "sol not defined"
                    >>> assert hasattr(sol, 't'), "sol should have attribute 't'"
                    >>> assert hasattr(sol, 'y'), "sol should have attribute 'y'"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test initial condition
                    >>> import numpy as np
                    >>> assert abs(sol.y[0, 0] - 0.0) < 0.01, "Initial concentration should be ~0"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test that concentration increases over time
                    >>> import numpy as np
                    >>> assert sol.y[0, -1] > sol.y[0, 0], "Concentration should increase over time"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test final concentration value
                    >>> assert 'CA_final' in dir(), "CA_final not defined"
                    >>> expected_final = 0.8  # Steady-state value
                    >>> assert abs(CA_final - expected_final) < 0.05, f"Final concentration {CA_final} should be near {expected_final}"
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
