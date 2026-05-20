import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil

        def helper(k:int, s:list) -> int:
            total = 0
            for i in s:
                total += ceil(i / k)
            return total

        def binary_search_left(s:list, h: int):
            l = 1
            r = max(s)
            result = -1
            while l <= r:
                mid = (l + r) // 2
                if helper(mid, s) <= h:
                    result = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return result

        return binary_search_left(piles, h)