class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        if not numSet:
            return 0
        
        if len(numSet) == 1:
            return 1

        maxLen = 0

        for num in numSet:
            if num - 1 not in numSet:
                currLen = 0
                while num in numSet:
                    currLen += 1
                    num += 1

                if currLen > maxLen:
                    maxLen = currLen
        
        return maxLen