class MinStack:

    def __init__(self):
        self.data = []
        self.minimum = []
        self.currMin = "nada"

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.currMin == "nada":
            self.currMin = val
        else:
            self.currMin = min(val, self.currMin)
        self.minimum.append(self.currMin)

    def pop(self) -> None:
        self.data.pop()
        self.minimum.pop()
        if len(self.minimum) != 0:
            self.currMin = self.minimum[len(self.minimum) - 1]
        else: 
            self.currMin = "nada"

    def top(self) -> int:
        return self.data[len(self.data) - 1]

    def getMin(self) -> int:
        return self.currMin
        
