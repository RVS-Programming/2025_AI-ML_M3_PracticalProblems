""" Question 11: collatz """
"""
Input: integer n
Output: number of steps it takes to reach 1 from n following the Collatz Conjecture
"""
def collatz(n):
    return

""" Test 11 """
def test_collatz():
    print("Testing collatz...", end='')
    assert(collatz(1) == 0)
    assert(collatz(2) == 1)
    assert(collatz(5) == 5)
    assert(collatz(11) == 14)
    assert(collatz(50) == 24)
    print("... done!")


if __name__ == '__main__':
    test_collatz()