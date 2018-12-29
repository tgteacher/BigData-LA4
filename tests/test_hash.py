import subprocess, os
from hash import hash as hsh

def test_hash():
    assert(hsh(123, 12, 7, 99)==6)
    
