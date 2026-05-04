class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = []
        for i in range(len(nums)): #starting number
            total = 0
            for j in range(i+1, len(nums)):
                total = nums[j] + nums[i]
                if total == target:
                    return [i, j]