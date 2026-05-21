class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary_search(s:list) -> int:
            l = 0
            r = len(s) - 1
            while l <= r:
                mid = (l + r) // 2
                if s[mid] == s[l]:
                    if s[mid] < s[r]:
                        return s[mid]
                    return s[r]
                elif s[mid] > s[l]:
                    if s[l] > s[r]:
                        l = mid + 1
                    else:
                        return s[l]
                else:
                    r = mid


        return binary_search(nums)