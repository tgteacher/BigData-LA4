import subprocess, os

def test_hash_list():
    command="python ./answers/hash_list.py 123 150 10 7 32"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(int(process.stdout.read().decode("utf-8"))==128)
