import subprocess, os
from answers import hash_band

def test_hash_band():
    env = {
        **os.environ,
        "PYTHONHASHSEED": str(0),
    }
    output = hash_band("./data/plants.data", 123, "qc", 12, 2, 2)
    assert(output==-6464292454374400732 or output==-8417330518760795669)
