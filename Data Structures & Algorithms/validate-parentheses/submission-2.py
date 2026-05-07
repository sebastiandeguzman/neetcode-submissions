class Solution:
    def isValid(self, s: str) -> bool:
        parens = []
        bracks = []
        squigs = []
        for i in s:
            if i in ["(", ")"]:
                parens.append(i)
            elif i in ["{", "}"]:
                squigs.append(i)
            else:
                bracks.append(i)
        if len(parens) % 2 != 0 or len(bracks) % 2 != 0 or len(squigs) % 2 != 0:
            return False
        open_paren = []
        open_brack = []
        open_squig = []
        for j in range(len(s)):
            if s[j] == "(":
                open_paren.append(j)
            elif s[j] == "[":
                open_brack.append(j)
            elif s[j] == "{":
                open_squig.append(j)
            elif s[j] == ")":
                if len(open_paren) < 1:
                    return False
                else:
                    for k in range(open_paren[-1]+1, j):
                        for l in range(len(open_paren)):
                            if open_paren[l] == k:
                                return False
                        for m in range(len(open_brack)):
                            if open_brack[m] == k:
                                return False
                        for n in range(len(open_squig)):
                            if open_squig[n] == k:
                                return False
                    del open_paren[-1]
            elif s[j] == "]":
                if len(open_brack) < 1:
                    return False
                else:
                    for k in range(open_brack[-1]+1, j):
                        for l in range(len(open_paren)):
                            if open_paren[l] == k:
                                return False
                        for m in range(len(open_brack)):
                            if open_brack[m] == k:
                                return False
                        for n in range(len(open_squig)):
                            if open_squig[n] == k:
                                return False
                    del open_brack[-1]
            else:
                if len(open_squig) < 1:
                    return False
                else:
                    for k in range(open_squig[-1]+1, j):
                        for l in range(len(open_paren)):
                            if open_paren[l] == k:
                                return False
                        for m in range(len(open_brack)):
                            if open_brack[m] == k:
                                return False
                        for n in range(len(open_squig)):
                            if open_squig[n] == k:
                                return False
                    del open_squig[-1]
        if len(open_paren) == 0 and len(open_brack) == 0 and len(open_squig) == 0:
            return True
        return False
        