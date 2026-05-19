class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for i in nums:
            if frequency.get(i) == None:
                frequency[i] = 1
            else:
                frequency[i] = frequency[i] + 1

        output = []

        for item in frequency.keys():
            if (len(output) < k):
                output.append(item)
            else:
                location = -1
                minimum = frequency[item]

                for i in range(len(output)):
                    if frequency[output[i]] < minimum:
                        minimum = frequency[output[i]]
                        location = i
                
                if location >= 0:
                    output[location] = item

        return output
            

