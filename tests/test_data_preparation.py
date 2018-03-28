import subprocess, os

def test_data_preparation():
    command="python ./answers/data_preparation.py ./data/plants.data urtica qc output-data-preparation.txt"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(open("output-data-preparation.txt","r").read()=="1"+os.linesep)
    
    command="python ./answers/data_preparation.py ./data/plants.data 'zinnia maritima' hi output-data-preparation.txt"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(open("output-data-preparation.txt","r").read()=="1"+os.linesep)

    command="python ./answers/data_preparation.py ./data/plants.data 'tephrosia candida' az output-data-preparation.txt"
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(open("output-data-preparation.txt","r").read()=="0"+os.linesep)

