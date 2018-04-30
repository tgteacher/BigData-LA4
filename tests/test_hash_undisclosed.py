import subprocess, os

def test_hash():
    command="python ./answers/hash.py 1234 19 11 91"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(int(process.stdout.read().decode("utf-8"))==5)
