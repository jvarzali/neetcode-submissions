class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest = max(piles)
        ceiling = math.ceil(largest / (h // len(piles)))
        floor = math.ceil(largest / (h - (len(piles) - 1)))
        mid = 0

        while ceiling > floor:
            mid = (ceiling + floor) // 2
            time = 0

            for i in range(len(piles)):
                time += math.ceil(piles[i] / mid)

            if time > h:
                floor = mid + 1
            else:
                ceiling = mid
            
        return floor