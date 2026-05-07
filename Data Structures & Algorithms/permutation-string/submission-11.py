class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for s in s1:
            if s not in s1_dict:
                s1_dict[s] = 1
            else:
                s1_dict[s] += 1
        s1_dict = dict(sorted(s1_dict.items(), key=lambda x: x[1]))
        for t in range(len(s2)):
            s2_dict = {s2[t] : 1}
            if s1_dict == dict(sorted(s2_dict.items(), key=lambda x: x[1])):
                return True 
            for j in range(t+1, len(s2)):
                if s2[j] not in s2_dict:
                    s2_dict[s2[j]] = 1
                else:
                    s2_dict[s2[j]] += 1
                if s1_dict == dict(sorted(s2_dict.items(), key=lambda x: x[1])):
                    return True 
        return False       
