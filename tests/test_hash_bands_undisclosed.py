import sys
sys.path.insert(0, './answers')
from answer import hash_bands


def test_hash_bands():
    out = hash_bands("./data/plants.data", 1234, 3, 4)
    with open("tests/test-hash-bands-undisclosed.txt", "w+") as f:
        f.write(out)
    assert(out==open("tests/test-hash-bands-undisclosed.txt","r").read())
