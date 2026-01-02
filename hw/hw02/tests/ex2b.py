test = {
    "name": "ex2b",
    "points": 6,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Test that CA_ss is calculated
                    >>> assert 'CA_ss' in dir(), "CA_ss not defined"
                    >>> assert 'CA_target' in dir(), "CA_target not defined"
                    >>> assert CA_target < CA_ss, "CA_target should be less than CA_ss"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test that event function is defined
                    >>> assert 'reach_target' in dir(), "reach_target function not defined"
                    >>> assert callable(reach_target), "reach_target should be a function"
                    >>> assert hasattr(reach_target, 'terminal'), "reach_target should have terminal attribute"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test t_95 is defined and reasonable
                    >>> assert 't_95' in dir(), "t_95 not defined"
                    >>> assert isinstance(t_95, (int, float, np.number)), "t_95 should be a number"
                    >>> assert 0 < t_95 < 60, f"t_95 = {t_95} should be between 0 and 60 min"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test t_95 value
                    >>> expected_t95 = 30.0  # Approximate value
                    >>> assert abs(t_95 - expected_t95) < 5, f"t_95 = {t_95} should be near {expected_t95} min"
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
