import subprocess, os
from answers import hash_bands

def test_hash_bands():
    out = hash_bands("./data/plants.data", 123, 5, 7)
    assert(out==open("tests/test-hash-bands-1.txt","r").read())
