class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lens = []
        freqs = {}
        for i in range(len(s)): #start
            freqs = {s[i]: 1}
            for j in range(i+1, len(s)): #end
                temp = []
                # print("")
                # print(f"trying range {i} to {j}")
                # print(f"trying values {s[i]} to {s[j]}")
                if s[j] not in freqs:
                    freqs[s[j]] = 1
                else:
                    freqs[s[j]] += 1
                for m in freqs:
                    temp.append(freqs[m])
                # print(f"This is temp: {temp}")
                temp.sort(reverse=True)
                pup = temp.pop(0)
                # print(f"This is temp after: {temp}")
                temp_count = 0
                for l in temp:
                    temp_count += l
                if temp_count <= k:
                    # print(f"appending {lens} with {(j-i)+1}")
                    lens.append((j-i) +1)
                    # print(f"new lens: {lens}")
        return sorted(lens, reverse=True)[0]
                
        