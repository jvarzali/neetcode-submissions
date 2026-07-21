class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window, maxes = [], []

        for num in nums[0:k]:
            self.insertStack(window, num)
        
        maxes.append(window[0])

        for l in range(len(nums) - k):
            r = l + k
            window.remove(nums[l])
            self.insertStack(window, nums[r])
            maxes.append(window[0])

        return maxes


    def insertStack(self, window: List[int], num: int) -> None:
        temp = []

        while window and window[len(window) - 1] < num:
                temp.append(window.pop())
            
        window.append(num)

        while temp:
            window.append(temp.pop())