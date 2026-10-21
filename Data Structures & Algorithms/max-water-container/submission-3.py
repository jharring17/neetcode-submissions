class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights) -1
        while left < right:
            new_area = min(heights[left], heights[right]) * (right - left)
            if new_area > max_area:
                max_area = new_area
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_area