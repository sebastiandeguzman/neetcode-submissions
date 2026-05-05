class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_string = 0
        for s_start in range(len(s)):
            used_chars = [s[s_start]]
            t = s[s_start]
            longest_string = max(len(t), longest_string)
            for s_end in range(s_start+1, len(s)):
                if len(t) > longest_string:
                    longest_string = len(t)
                if s[s_end] not in used_chars:
                    used_chars.append(s[s_end])
                    t = f"{t}{s[s_end]}"
                else:
                    t = ""
                    used_chars.clear()
                    break
            longest_string = max(len(t), longest_string)

        return longest_string