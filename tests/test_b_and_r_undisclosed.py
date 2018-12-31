from answers import get_b_and_r as br


def test_b_and_r():
    out = br(10, 0.5)
    assert(out==open("tests/test-get-b-and-r-undisclosed.txt","r").read())
