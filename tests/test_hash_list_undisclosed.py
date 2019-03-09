import sys
sys.path.insert(0, './answers')
from answer import hash_list as hl

def test_hash_list():
    assert(hl(1234, 125, 17, 4, 12)==66)
