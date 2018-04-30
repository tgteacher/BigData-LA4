import subprocess, os

def test_primes():
    command="python ./answers/primes.py 25 23"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/test-primes-undisclosed.txt","r").read())
