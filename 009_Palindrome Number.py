# Given an integer x, return true if x is a palindrome, and false otherwise.

# Runtime 40 ms Beats 95.93%
# Memory 13.2 MB Beats 96.18%


class Solution(object):
    @staticmethod
    def isPalindrome(x):
        x = str(x)
        rev = x[::-1]
        if rev == x:
            return True
        else:
            return False