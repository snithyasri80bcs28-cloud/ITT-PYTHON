class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        
        first = 1   # ways to reach step 1
        second = 2  # ways to reach step 2
        
        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current
        
        return second


# Example usage
obj = Solution()
print(obj.climbStairs(2))  # Output: 2
print(obj.climbStairs(3))  # Output: 3
