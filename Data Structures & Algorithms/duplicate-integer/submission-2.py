class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        chars = []
        for i in nums:
            if i not in chars:
                chars.append(i)
            else:
                return True
        return False