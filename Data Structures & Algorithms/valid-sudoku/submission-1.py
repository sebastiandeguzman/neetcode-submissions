class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for i in board:
            print(i)
            used_nums = []
            for j in i:
                if j != ".":
                    if j in used_nums:
                        return False
                    used_nums.append(j)

        #check columns
        used_nums = []
        for k in range(9): #specific index
            used_nums = []
            for l in board: #iterating over each list
                if l[k] != ".":
                    if l[k] in used_nums:
                        return False
                    used_nums.append(l[k])

        #check boxes
        used_nums = []
        x, y, p, q = 0, 3, 0, 3
        while y <= 9: #rows
            while q <= 9: #columns
                for n in range(x, y): #rows
                    for m in range(p, q): #columns
                        if board[n][m] != ".":
                            if board[n][m] in used_nums:
                                return False
                            used_nums.append(board[n][m])
                    print(f"used_nums = {used_nums}")
                used_nums.clear()
                p += 3
                q += 3
            x += 3
            y += 3
                

        return True