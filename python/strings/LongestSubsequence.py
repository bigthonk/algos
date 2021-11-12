class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_dict = {}
        max_len = 0
        start_idx = 0

        for i, char in enumerate(s):
            if char in last_dict:
                start_idx = max(start_idx, last_dict[char] + 1)

            max_len = max(max_len, i-start_idx + 1)

            last_dict[char] = i

        return max_len
