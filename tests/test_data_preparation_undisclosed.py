from answers import data_preparation as dp
import os

def test_data_preparation():
    dp("./data/plants.data", "agnorhiza", "nc", "output-data-preparation.txt")
    assert(open("output-data-preparation.txt","r").read()=="0"+os.linesep)
    
    dp("./data/plants.data", "carex globosa", "ca", "output-data-preparation.txt")
    assert(open("output-data-preparation.txt","r").read()=="1"+os.linesep)

    dp("./data/plants.data", "lawsonia", "qc", "output-data-preparation.txt")
    assert(open("output-data-preparation.txt","r").read()=="0"+os.linesep)

