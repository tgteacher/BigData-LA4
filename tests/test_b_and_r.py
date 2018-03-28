import subprocess, os

def test_b_and_r():
    command="python ./answers/get_b_and_r.py 100 0.8"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/test-get-b-and-r.txt","r").read())
