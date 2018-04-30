import subprocess, os

def test_hash_list():
    command="python ./answers/hash_list.py 1234 125 17 4 12"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(int(process.stdout.read().decode("utf-8"))==66)
