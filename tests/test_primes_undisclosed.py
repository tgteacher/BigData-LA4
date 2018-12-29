import subprocess, os
from primes import primes

def test_primes():
    assert(primes(25, 23)==
        [int(el.strip())
            for el in open("tests/test-primes-undisclosed.txt","r")])
