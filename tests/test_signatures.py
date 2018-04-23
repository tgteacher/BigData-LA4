import subprocess, os

def test_signatures():
    command="python ./answers/signatures.py ./data/plants.data 123 10 qc"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    output = process.stdout.read().decode("utf-8").strip()
    assert(output==open("tests/test-signatures.txt","r").read().strip() or
           output==open("tests/test-signatures-1.txt","r").read().strip())
