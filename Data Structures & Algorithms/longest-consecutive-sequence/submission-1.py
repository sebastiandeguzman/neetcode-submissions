class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        print(f"sorted nums = {nums}")
        consec = []
        lens = []
        for n in nums:
            print(f"starting with {n}")
            if n-1 not in consec:
                print(f"{n-1} not in consec")
                lens.append(len(consec))
                consec.clear()
            consec.append(n)
        lens.append(len(consec))
        return sorted(lens, reverse=True)[0]