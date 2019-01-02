from answers import hash_band

def test_hash_band():
    result = hash_band("./data/plants.data", 1234, "ca", 6, 3, 2)
    assert(result==1871990837703389805 or result==4239803293702038060)
