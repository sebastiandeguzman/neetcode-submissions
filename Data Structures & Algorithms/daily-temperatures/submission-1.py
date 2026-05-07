class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        biggest_indexes = {}
        for i in range(len(temperatures)):
            biggest_indexes[i] = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    biggest_indexes[i] = j-i
                    break       
        final_list = []
        for k in biggest_indexes:
            final_list.append(biggest_indexes[k])
        return final_list