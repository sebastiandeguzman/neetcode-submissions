class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        copy = nums
        for i in range(len(nums)):
            mult = 1
            remove = copy.pop(i)
            for j in copy:
                mult *= j
            final.append(mult)
            copy.insert(i, remove)
        return final