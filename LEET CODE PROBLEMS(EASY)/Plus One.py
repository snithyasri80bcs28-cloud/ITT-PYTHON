class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        n = len(digits)
        
        # Traverse from last digit
        for i in range(n - 1, -1, -1):
            
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0  # if digit is 9, make it 0 and continue
        
        # If all digits were 9
        return [1] + digits


# Example usage
obj = Solution()
print(obj.plusOne([1,2,3]))  # Output: [1,2,4]
print(obj.plusOne([9]))      # Output: [1,0]
print(obj.plusOne([9,9,9]))  # Output: [1,0,0,0]
