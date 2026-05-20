class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                area = -(i-j)*min(heights[i], heights[j]) if i < j else (i-j)*min(heights[i], heights[j])
                if area > maxArea:
                    maxArea = area
        return maxArea
        