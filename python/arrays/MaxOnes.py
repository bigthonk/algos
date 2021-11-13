class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        start_index = 0
        nums += ["end"]
        
        for index, value in enumerate(nums):
            if value == 0:
                current_len = index - start_index
                max_len = max(max_len, current_len)
                start_index = index + 1
                
            if value == "end":
                current_len = index - start_index
                max_len = max(max_len, current_len)
                
        return max_len
