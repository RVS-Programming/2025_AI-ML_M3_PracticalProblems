from q5_longest_string_length import longest_string_length 

def test_longest_string_length():
    L0 = ["hi", "hello", "howdy"]
    assert(longest_string_length(L0) == 5)
    L1 = ["hello", "goodbye", "pineapple"]
    assert(longest_string_length(L1) == 9)
    L2 = ["a", "b", "c"]
    assert(longest_string_length(L2) == 1)
    
