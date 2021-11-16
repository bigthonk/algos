class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 1,1
        results = [1]*n
        i = 0
        while i < n:
            results[i] *= left
            left *= nums[i]
            results[n -1 -i] *= right
            right *= nums[n -1 -i]
            i += 1
        return results
