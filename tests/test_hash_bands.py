import sys
sys.path.insert(0, './answers')
from answer import hash_bands

def test_hash_bands():
    out = hash_bands("./data/plants.data", 123, 5, 7)
    assert(out==open("tests/test-hash-bands.txt","r").read())
