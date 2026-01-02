test = {
    "name": "ex3b",
    "points": 3,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> # Test that product_yield is defined
                    >>> assert 'product_yield' in dir(), "product_yield not defined"
                    >>> assert isinstance(product_yield, (int, float, np.number)), "product_yield should be a number"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test product_yield is positive and reasonable
                    >>> assert product_yield > 0, "product_yield should be positive"
                    >>> assert product_yield < 5, f"product_yield = {product_yield} seems too high"
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> # Test product_yield value
                    >>> expected_yield = 1.2  # Approximate value based on q2=0.25 and residence time
                    >>> assert abs(product_yield - expected_yield) < 0.5, f"product_yield = {product_yield} should be near {expected_yield}"
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
