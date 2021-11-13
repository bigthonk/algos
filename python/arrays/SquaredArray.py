class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        index_1, index_2 = 0, len(nums)-1
        squared_sequence = [0] * len(nums)
        new_index = len(nums)-1
        
        while new_index >= 0:
            if abs(nums[index_1]) > abs(nums[index_2]):
                squared_sequence[new_index] = nums[index_1] ** 2
                index_1 +=1
                new_index -=1
            else:
                squared_sequence[new_index] = nums[index_2] ** 2
                index_2 -=1
                new_index -=1
        
        return squared_sequence
