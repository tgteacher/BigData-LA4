import subprocess, os
from answers import hash_list as hl

def test_hash_list():
    assert(hl(123, 150, 10, 7, 32)==61)
