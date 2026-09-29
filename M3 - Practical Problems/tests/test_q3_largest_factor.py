from q3_largest_factor import largest_factor 

def test_largest_factor():
    assert(largest_factor(1) == 1)
    assert(largest_factor(12) == 6)
    assert(largest_factor(25) == 5)
    assert(largest_factor(31) == 1)
    assert(largest_factor(117) == 39)
    
