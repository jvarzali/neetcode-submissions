class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos, spd = zip(*sorted(zip(position, speed), reverse=True))
        print(pos)
        print(spd)
        slowest, total = None, len(pos)

        for i in range(len(position)):
            time = (target - pos[i]) / spd[i]
            print(i)
            print(str(target) + " " + str(pos[i]) + " " + str(spd[i]))
            print((target - position[i]) / speed[i])
            print(time)
            print(slowest)
            print(total)
            
            if slowest == None:
                slowest = time
            elif time <= slowest:
                total -= 1
            else:
                slowest = time

            print(total)
            print()

        return total
        
        
        # fleets, start = [], []
        

        # for i in range(len(position)):
        #     curr = (target - position[i]) / speed[i]
        #     end = len(fleets) - 1
        #     tempFleets, tempStart = [], []
            
        #     while True:
        #         if end == -1:
        #             fleets.append(curr)
        #             start.append(position[i])
        #             break
        #         elif (curr <= fleets[end] and position[i] < start[end]):
        #             break
        #         elif (curr >= fleets[end] and position[i] > start[end]):
        #             fleets[end] = curr
        #             start[end] = position[i]
        #             break
        #         elif curr > fleets[end] and position[i] < start[end]:
        #             fleets.append(curr)
        #             start.append(position[i])
        #             break
        #         else:
        #             tempFleets.append(fleets.pop())
        #             tempStart.append(start.pop())
        #             end -= 1

        #     while len(tempFleets) > 0:
        #         fleets.append(tempFleets.pop())
        #         start.append(tempStart.pop())
        
        # print(fleets)
        # print(start)
        # return len(fleets)