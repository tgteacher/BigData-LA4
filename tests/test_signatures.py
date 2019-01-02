from answers import signatures as sig

def test_signatures():
    result=sig("./data/plants.data", 123, 10, "qc")
    assert(result=={int(line.split(': ')[0]): int(line.strip().split(': ')[1])
                    for line in open("tests/test-signatures.txt","r")}
           or result=={int(line.split(': ')[0]): int(line.strip().split(': ')[1])
                       for line in open("tests/test-signatures-1.txt","r")})
