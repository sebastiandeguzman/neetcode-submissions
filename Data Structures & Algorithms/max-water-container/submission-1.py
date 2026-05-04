class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for height_start in range(len(heights)): #starting
            for height_end in range(height_start + 1, len(heights)):
                temp_area = min(heights[height_end], heights[height_start])*(height_end - height_start)
                if temp_area > area:
                    area = temp_area
        return area