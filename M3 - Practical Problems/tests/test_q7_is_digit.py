from q7_is_digit import is_digit 

def test_is_digit():
    assert(is_digit("") == False)
    assert(is_digit("1") == True)
    assert(is_digit("123a") == False)
    assert(is_digit("99923") == True)
    assert(is_digit("abcd") == False)

