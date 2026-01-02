test = {
    "name": "ex4a",
    "points": 12,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Test that dXdt function is defined
                    >>> assert 'dXdt' in dir(), "dXdt function not defined"
                    >>> assert callable(dXdt), "dXdt should be a function"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test that sol_underdamped is defined
                    >>> assert 'sol_underdamped' in dir(), "sol_underdamped not defined"
                    >>> assert hasattr(sol_underdamped, 't'), "sol_underdamped should have attribute 't'"
                    >>> assert hasattr(sol_underdamped, 'y'), "sol_underdamped should have attribute 'y'"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test initial condition
                    >>> import numpy as np
                    >>> assert abs(sol_underdamped.y[0, 0] - 20) < 0.1, "Initial h should be 20 cm"
                    >>> assert abs(sol_underdamped.y[1, 0] - 0) < 0.1, "Initial v should be 0 cm/min"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test that solution oscillates (check for sign changes)
                    >>> import numpy as np
                    >>> sign_changes = np.sum(np.diff(np.sign(sol_underdamped.y[0])) != 0)
                    >>> assert sign_changes >= 3, f"Underdamped solution should oscillate (found {sign_changes} sign changes)"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test h_final_underdamped
                    >>> assert 'h_final_underdamped' in dir(), "h_final_underdamped not defined"
                    >>> assert abs(h_final_underdamped) < 5, f"Final deviation should be near 0, got {h_final_underdamped}"
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
