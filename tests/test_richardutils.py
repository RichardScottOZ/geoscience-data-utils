from richardutils import richardfunction


EPSILON = 1e-9

def test_richardfunction():
    """
    Test that our roots are square.
    """
    assert abs(richardfunction(1000) - 31.6227766017) < EPSILON
