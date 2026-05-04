class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diff_nums = []
        dictionary = {}
        amount_of_nums = 0
        for i in nums:
            if i not in diff_nums:
                dictionary[i] = 1
                diff_nums.append(i)
            else:
                dictionary[i] += 1
        dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
        semifinal = []
        for j in dictionary:
            semifinal.append(j)
        final = []
        for m in range(k):
            final.append(semifinal[m])
        return final
