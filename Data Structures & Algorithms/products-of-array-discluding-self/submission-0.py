class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1 for i in range(len(nums) + 1)]
        backward = [1 for i in range(len(nums) + 1)]
        result = []

        for i in range(1, len(nums) + 1):
            forward[i] = forward[i-1] * nums[i - 1]
            backward[len(backward) - i - 1] = backward[len(backward) - i] * nums[len(nums) - i]
        
        print(forward, backward)

        for i in range(0, len(forward) - 1):
            result.append(forward[i] * backward[i + 1])

        return result