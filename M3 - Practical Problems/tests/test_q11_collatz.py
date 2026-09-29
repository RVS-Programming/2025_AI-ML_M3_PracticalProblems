from q11_collatz import collatz 

def test_collatz():
    assert(collatz(1) == 0)
    assert(collatz(2) == 1)
    assert(collatz(5) == 5)
    assert(collatz(11) == 14)
    assert(collatz(50) == 24)
    
