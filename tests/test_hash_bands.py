import subprocess, os

def test_hash_bands():
    command="setenv PYTHONHASHSEED 0; python ./answers/hash_bands.py ./data/plants.data 123 5 7"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/test-hash-bands.txt","r").read())
