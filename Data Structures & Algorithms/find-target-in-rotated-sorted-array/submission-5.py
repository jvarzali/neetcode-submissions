class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = math.floor((l + r) / 2)

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        minimum = r
        l, r = 0, len(nums) - 1

        if target > nums[r]:
            r = minimum - 1
        else:
            l = minimum

        while l <= r:
            mid = math.floor((l + r) / 2)

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return -1