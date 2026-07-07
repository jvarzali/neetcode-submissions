class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp, index, result = [], [], [None] * len(temperatures)

        for i in range(len(temperatures)):
            while len(temp) > 0 and temperatures[i] > temp[len(temp) - 1]:
                temp.pop()
                location = index.pop()
                result[location] = i - location
            temp.append(temperatures[i])
            index.append(i)

        for i in range(len(index)):
            result[index[i]] = 0

        return result