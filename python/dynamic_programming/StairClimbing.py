class Solution:
    def climbStairs(self, n: int) -> int:
        current = 0
        num_ways = [1]
        maxSteps = 2
	
        for current_step in range(1,n+1):
            prev_window_start = current_step - maxSteps - 1
            window_end = current_step - 1

            if prev_window_start >= 0:
                current -= num_ways[prev_window_start]

            current += num_ways[window_end]
            num_ways.append(current)

        return num_ways[n]
