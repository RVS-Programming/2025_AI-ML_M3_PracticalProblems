""" Question 2: smallest_factor """
"""
Input: integer n
Output: smallest factor of n greater than 1
"""
def smallest_factor(n):
    return

""" Test 2 """
def test_smallest_factor():
    print("Testing smallest_factor...", end='')
    assert(smallest_factor(1) == 1)
    assert(smallest_factor(6) == 2)
    assert(smallest_factor(15) == 3)
    assert(smallest_factor(29) == 29)
    assert(smallest_factor(117) == 3)
    print("... done!")


if __name__ == '__main__':
    test_smallest_factor()
