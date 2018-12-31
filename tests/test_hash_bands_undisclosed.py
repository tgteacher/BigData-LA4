from answers import hash_bands


def test_hash_bands():
    out = hash_bands("./data/plants.data", 1234, 3, 4)
    assert(out==open("tests/test-hash-bands-undisclosed.txt","r").read())
