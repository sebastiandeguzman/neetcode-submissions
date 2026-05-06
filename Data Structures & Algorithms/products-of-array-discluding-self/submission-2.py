class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(len(nums)):
            mult = 1
            remove = nums.pop(i)
            for j in nums:
                mult *= j
            final.append(mult)
            nums.insert(i, remove)
        return final