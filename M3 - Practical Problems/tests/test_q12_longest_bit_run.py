from q12_longest_bit_run import longest_bit_run 

def test_longest_bit_run():
    assert(longest_bit_run('0') == 1)
    assert(longest_bit_run('011') == 2)
    assert(longest_bit_run('0000') == 4)
    assert(longest_bit_run('01') == 1)
    assert(longest_bit_run('00111100') == 4)
   
