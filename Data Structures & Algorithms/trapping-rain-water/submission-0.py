class Solution:
    def trap(self, heights: List[int]) -> int:
        l, r, height, area = 0, len(heights) - 1, 0, 0

        while l < r:
            if heights[l] > height and heights[r] > height:
                tempHeight = min(heights[l], heights[r])

                for i in range(l + 1, r):
                    if heights[i] < tempHeight:
                        area += tempHeight - max(height, heights[i])

                height = tempHeight
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return area