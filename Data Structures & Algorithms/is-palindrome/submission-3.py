class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        t = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                t = f"{t}{i}"
        return t == t[::-1]