""" Question 3: largest_factor """
"""
Input: integer n
Output: largest factor of n less than n itself
"""
def largest_factor(n):
    return

""" Test 3 """
def test_largest_factor():
    print("Testing largest_factor...", end='')
    assert(largest_factor(1) == 1)
    assert(largest_factor(12) == 6)
    assert(largest_factor(25) == 5)
    assert(largest_factor(31) == 1)
    assert(largest_factor(117) == 39)
    print("... done!")


if __name__ == '__main__':
    test_largest_factor()
