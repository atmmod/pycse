test = {
    "name": "ex3a",
    "points": 15,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Test that dYdt function is defined
                    >>> assert 'dYdt' in dir(), "dYdt function not defined"
                    >>> assert callable(dYdt), "dYdt should be a function"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test that sol_bioreactor is defined
                    >>> assert 'sol_bioreactor' in dir(), "sol_bioreactor not defined"
                    >>> assert hasattr(sol_bioreactor, 't'), "sol_bioreactor should have attribute 't'"
                    >>> assert hasattr(sol_bioreactor, 'y'), "sol_bioreactor should have attribute 'y'"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test solution shape
                    >>> import numpy as np
                    >>> assert sol_bioreactor.y.shape[0] == 4, "Solution should have 4 state variables"
                    >>> assert sol_bioreactor.y.shape[1] == 200, "Solution should have 200 time points"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test that X1_final and P2_final are defined
                    >>> assert 'X1_final' in dir(), "X1_final not defined"
                    >>> assert 'P2_final' in dir(), "P2_final not defined"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test X1_final value (growth phase should have high biomass)
                    >>> assert X1_final > 1.0, f"X1_final = {X1_final} should be > 1.0"
                    >>> assert X1_final < 5.0, f"X1_final = {X1_final} should be < 5.0"
                    """,
                    "hidden": True,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test P2_final value (production phase should have higher product)
                    >>> assert P2_final > 0.5, f"P2_final = {P2_final} should be > 0.5"
                    >>> assert P2_final < 3.0, f"P2_final = {P2_final} should be < 3.0"
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
