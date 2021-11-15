class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for index, number in list(enumerate(nums)):
            if number != val:
                nums[count] = number
                count += 1
        return count
