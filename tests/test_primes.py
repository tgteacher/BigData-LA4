from answers import primes

def test_primes():
    assert(primes(50, 41)==
            [int(el.strip()) for el in open("tests/test-primes.txt","r")])
