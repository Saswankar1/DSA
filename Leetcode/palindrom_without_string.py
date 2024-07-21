class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Numbers ending in 0 (except 0 itself) are not palindromes
        if x % 10 == 0 and x != 0:
            return False
        
        reversed_half = 0
        while x > reversed_half:
            last_digit = x % 10
            reversed_half = reversed_half * 10 + last_digit
            x = x // 10
        
        # When the length is an odd number, we can get rid of the middle digit by reversed_half // 10
        return x == reversed_half or x == reversed_half // 10

# Example usage
solution = Solution()
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121)) # Output: False
print(solution.isPalindrome(10))   # Output: False
