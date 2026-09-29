from q4_num_odd_digits import num_odd_digits 

def test_num_odd_digits():
    assert(num_odd_digits(0) == 0)
    assert(num_odd_digits(1) == 1)
    assert(num_odd_digits(13) == 2)
    assert(num_odd_digits(2265) == 1)
    assert(num_odd_digits(2468) == 0)
    assert(num_odd_digits(13355) == 5)
    
