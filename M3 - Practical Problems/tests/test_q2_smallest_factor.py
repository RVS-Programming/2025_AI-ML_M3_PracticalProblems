from q2_smallest_factor import smallest_factor 

def test_smallest_factor():
    assert(smallest_factor(1) == 1)
    assert(smallest_factor(6) == 2)
    assert(smallest_factor(15) == 3)
    assert(smallest_factor(29) == 29)
    assert(smallest_factor(117) == 3)
    
