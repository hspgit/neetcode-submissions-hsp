class Solution:
    def trap(self, height: List[int]) -> int:
        # max_left = [0] * len(height)
        # max_right = [0] * len(height)
        

        
        # for i in range(1, len(height)):
        #     max_left[i] = max(max_left[i-1], height[i-1])

        # for i in range(len(height)-2, -1, -1):
        #     max_right[i] = max(max_right[i+1], height[i+1])
        
        # min_left_right = [min(max_left[i], max_right[i]) for i in range(len(height))]

        # total = 0

        # for i in range(len(height)):
        #     total = total + max(0, min_left_right[i] - height[i])

        # return total

        l, r = 0, len(height) - 1
        left_max = height[l]
        right_max = height[r]
        total = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                total += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                total += right_max - height[r]
        
        return total






