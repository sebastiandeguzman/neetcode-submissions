class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anas = []
        final_list = []
        new_strs = {}
        for word in strs:
            sorted_str = sorted(word)
            new_str = ""
            for m in sorted_str:
                new_str = f"{new_str}{m}"
            if new_str in new_strs:
                new_strs[new_str] = list(new_strs[new_str])
                new_strs[new_str].append(word)
            else:
                new_strs[new_str] = [word]
        for k in new_strs:
            final_list.append(new_strs[k])
        return sorted(final_list, key=len, reverse=True)
        
        #sorted list - sorted list of all words (sorted also by chars)
