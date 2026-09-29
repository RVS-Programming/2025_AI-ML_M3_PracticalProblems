from q6_avg_of_primes import average_of_primes 

import math
def test_average_of_primes():
    assert(average_of_primes([]) == 0)
    assert(average_of_primes([2]) == 2)
    assert(average_of_primes([1, 2, 3]) == 2.5)
    assert(average_of_primes([4, 6, 8]) == 0)
    assert(average_of_primes([2, 3, 5, 7, 11]) == 5.6)
    
