import subprocess, os

def test_signatures():
    command="python ./answers/signatures.py ./data/plants.data 123 10 qc"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8").strip()==open("tests/test-signatures.txt","r").read().strip())
