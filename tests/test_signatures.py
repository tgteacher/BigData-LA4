import subprocess, os

def test_hash_signatures():
    command="python ./answers/signatures.py ./data/plants.data 123 10 qc"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8").strip()=="{0: 24, 1: 2, 2: 13, 3: 3, 4: 12, 5: 9, 6: 4, 7: 1, 8: 3, 9: 0, 'state': 'qc'}")
