import os, sys
sys.path.insert(0, './answers')
from answer import data_preparation as dp

def test_data_preparation():
    a = dp("./data/plants.data", "urtica", "qc", "output-data-preparation.txt")
    assert(a==1)

    a = dp("./data/plants.data", "zinnia maritima", "hi", "output-data-preparation.txt")
    assert(a==1)

    a = dp("./data/plants.data", "tephrosia candida", "az", "output-data-preparation.txt")
    assert(a==0)
