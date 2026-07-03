class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        out = []

        for i in range(len(nums) - 2): 
            if nums[i] <= 0:
                k = len(nums) - 1
                j = i + 1
                while j < k:
                    if nums[i] + nums[k] + nums[j] == 0:
                        if [nums[i], nums[j], nums[k]] not in out:
                            out.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -=1
                    elif nums[i] + nums[k] + nums[j] < 0: 
                        j += 1
                    else:
                        k -= 1
            else:
                break


        return out

