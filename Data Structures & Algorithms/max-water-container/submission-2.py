class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxArea = 0
        while l < r:
            area = (r-l)*min(heights[l], heights[r])
            if area > maxArea:
                maxArea = area
            if heights[l] > heights[r]:
                l,r = l, r-1
            else:
                l,r = l+1, r
        return maxArea
        