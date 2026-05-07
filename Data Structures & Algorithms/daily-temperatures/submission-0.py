class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        biggest_indexes = {}
        for i in range(len(temperatures)):
            print(f"trying master value {temperatures[i]} at {i}")
            biggest_indexes[i] = 0
            for j in range(i+1, len(temperatures)):
                print(f"trying second value {temperatures[j]} at {j}")
                if temperatures[j] > temperatures[i]:
                    print(f"{temperatures[j]} is bigger than {temperatures[i]}")
                    biggest_indexes[i] = j-i
                    break
                
        final_list = []
        for k in biggest_indexes:
            final_list.append(biggest_indexes[k])
        return final_list