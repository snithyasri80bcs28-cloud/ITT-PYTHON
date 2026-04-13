class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # Negative numbers are not palindrome
        # Numbers ending with 0 (except 0 itself) are not palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        # Reverse half of the number
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x = x // 10
        
        # For even digits: x == reversed_half
        # For odd digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10


# Example usage
obj = Solution()
print(obj.isPalindrome(121))   # True
print(obj.isPalindrome(-121))  # False
print(obj.isPalindrome(10))    # False
