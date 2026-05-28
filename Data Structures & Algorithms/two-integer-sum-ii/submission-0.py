class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lower = 0
        upper = len(numbers) - 1

        while True:
            if numbers[lower] + numbers[upper] == target:
                return [lower + 1, upper + 1]
            elif numbers[lower] + numbers[upper] > target:
                upper -= 1
            else:
                lower += 1
            
            