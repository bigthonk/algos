class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens = 0
        for num in nums:
            if len(str(num))%2 == 0:
                evens+=1
        return evens
