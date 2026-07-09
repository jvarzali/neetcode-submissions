class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos, spd = zip(*sorted(zip(position, speed), reverse=True))
        slowest, total = None, len(pos)

        for i in range(len(position)):
            time = (target - pos[i]) / spd[i]
            
            if slowest == None:
                slowest = time
            elif time <= slowest:
                total -= 1
            else:
                slowest = time

        return total
        
  