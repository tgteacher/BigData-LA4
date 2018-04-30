import subprocess, os

def test_hash_band():
    env = {
        **os.environ,
        "PYTHONHASHSEED": str(0),
    }
    command="python ./answers/hash_band.py ./data/plants.data 1234 ca 6 3 2"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    code=process.wait()
    assert(not code), "Command failed"
    result = int(process.stdout.read().decode("utf-8"))
    assert(result==1871990837703389805 or result==4239803293702038060)
