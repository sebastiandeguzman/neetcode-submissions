class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)): #first number
            for j in range(i, len(numbers)): #second number
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]