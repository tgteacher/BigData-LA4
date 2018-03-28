import subprocess, os

def test_hash_band():
    command="setenv PYTHONHASHSEED 0 ; python ./answers/hash_band.py ./data/plants.data 123 qc 12 2 2"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(int(process.stdout.read().decode("utf-8"))==-6464292454374400732)
