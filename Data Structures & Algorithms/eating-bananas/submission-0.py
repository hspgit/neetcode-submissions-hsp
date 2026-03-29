class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_speed = r

        while l <= r:
            m = (l + r) // 2
            curr_time = sum(math.ceil(pile/m) for pile in piles)

            if curr_time <= h:
                min_speed = m
                r = m - 1
            else:
                l = m + 1

        return min_speed 