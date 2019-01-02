from answers import signatures as sig

def test_signatures():
    result = sig("./data/plants.data", 1234, 12, "ca")
    assert(result=={int(line.split(': ')[0]): int(line.strip().split(': ')[1])
                    for line in
                    open("tests/test-signatures-undisclosed.txt","r")})
