class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        inital_len = len(arr)
        index = 0
        
        while index < inital_len -1:
            if arr[index] == 0:
                arr.insert(index,0)
                del(arr[-1])
                index += 2
            else:
                index += 1
