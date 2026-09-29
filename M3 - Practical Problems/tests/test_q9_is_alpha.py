from q9_is_alpha import is_alpha 

def test_is_alpha():
    assert(is_alpha("") == False)
    assert(is_alpha("a") == True)
    assert(is_alpha("123a") == False)
    assert(is_alpha("Hello") == True)
    assert(is_alpha("hello!") == False)
    
