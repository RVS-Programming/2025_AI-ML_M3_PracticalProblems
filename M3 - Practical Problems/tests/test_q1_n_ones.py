from q1_n_ones import n_ones 

def test_n_ones():
    assert(n_ones(0) == 0)
    assert(n_ones(1) == 1)
    assert(n_ones(4) == 1111)
    assert(n_ones(7) == 1111111)
    
