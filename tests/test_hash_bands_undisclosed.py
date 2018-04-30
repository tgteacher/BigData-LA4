import subprocess, os

def test_hash_bands():
    env = {
        **os.environ,
        "PYTHONHASHSEED": str(0),
    }
    command="python ./answers/hash_bands.py ./data/plants.data 1234 3 4"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/test-hash-bands-undisclosed.txt","r").read())
