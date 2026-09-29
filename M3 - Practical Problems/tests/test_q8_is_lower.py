from q8_is_lower import is_lower 

def test_is_lower():
    assert(is_lower("") == False)
    assert(is_lower("a") == True)
    assert(is_lower("123a") == True)
    assert(is_lower("Hello") == False)
    assert(is_lower("hello!") == True)
    
