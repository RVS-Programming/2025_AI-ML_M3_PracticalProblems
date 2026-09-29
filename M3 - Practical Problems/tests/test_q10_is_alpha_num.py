from q10_is_alpha_num import is_alpha_num 

def test_is_alpha_num():
    assert(is_alpha_num("") == False)
    assert(is_alpha_num("a") == True)
    assert(is_alpha_num("123a") == True)
    assert(is_alpha_num("Hello") == True)
    assert(is_alpha_num("hello!") == False)
    
