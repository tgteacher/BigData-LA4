from answers import data_preparation as dp
import os

def test_data_preparation():
    dp("./data/plants.data", "urtica", "qc", "output-data-preparation.txt")
    assert(open("output-data-preparation.txt","r").read()=="1"+os.linesep)
    
    dp("./data/plants.data", "zinnia maritima", "hi", "output-data-preparation.txt")
    assert(open("output-data-preparation.txt","r").read()=="1"+os.linesep)

    dp("./data/plants.data", "tephrosia candida", "az", "output-data-preparation.txt")
    assert(open("output-data-preparation.txt","r").read()=="0"+os.linesep)
