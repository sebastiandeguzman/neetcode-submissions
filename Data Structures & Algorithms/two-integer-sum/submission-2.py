class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): #starting number
            total = 0
            for j in range(i+1, len(nums)):
                if nums[j] + nums[i] == target:
                    return [i, j]