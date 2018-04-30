import subprocess, os

def test_hash_band():
    env = {
        **os.environ,
        "PYTHONHASHSEED": str(0),
    }
    command="python ./answers/hash_band.py ./data/plants.data 123 qc 12 2 2"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    code=process.wait()
    assert(not code), "Command failed"
    output = int(process.stdout.read().decode("utf-8"))
    assert(output==-6464292454374400732 or output==-8417330518760795669)
