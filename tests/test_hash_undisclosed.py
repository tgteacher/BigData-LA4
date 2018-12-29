import subprocess, os
from hash import hash as hsh

def test_hash():
    assert(hsh(1234, 19, 11, 91)==5)
