from sigma import code_to_string


def test_readme_example():
    assert (
        code_to_string("12.2")
        == "[12.2] Power up sequence fault: Traction: Forward switch active at power up"
    )
    assert (
        code_to_string("18.3", include_code=False)
        == "High sided mosfets short circuit: M3 mosfets"
    )


def test_lambdas():
    assert (
        code_to_string("7-199", include_code=False)
        == "Adjustment out of range: First digit: menu number, Last 2 digits: adjustment number within menu"
    )
    assert (
        code_to_string("7-99", include_code=False)
        == "Adjustment out of range: <unknown>"
    )
