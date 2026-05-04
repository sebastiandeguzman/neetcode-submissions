class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for height_start in range(len(heights)): #starting
            for height_end in range(height_start + 1, len(heights)):
                temp_area = min(heights[height_end], heights[height_start])*(height_end - height_start)
                if temp_area > area:
                    print(f"temp area of {temp_area} achieved w/ bars {height_start} and {height_end}")
                    print(f"height of height_start = {heights[height_start]}")
                    print(f"height of height_end = {heights[height_end]}")
                    area = temp_area
        return area