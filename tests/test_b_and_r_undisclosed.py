import subprocess, os

def test_b_and_r():
    command="python ./answers/get_b_and_r.py 10 0.5"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/test-get-b-and-r-undisclosed.txt","r").read())
