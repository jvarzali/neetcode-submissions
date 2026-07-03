class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        j = len(heights) - 1

        # for i in range(len(heights) - 1):
        #     for j in range(i + 1, len(heights)):
        #         currVolume = min(heights[i], heights[j]) * (j - i)
        #         volume = max(volume, currVolume)
        
        i = 0
        while i < j:
            volume = max(volume, (j - i) * min(heights[j], heights[i]))
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return volume
