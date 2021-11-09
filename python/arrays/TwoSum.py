class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        
        for number_index, number in enumerate(nums):
            if target - number in previous:
                    return [number_index,previous[target-number]]
            else:
                previous[number] = number_index
