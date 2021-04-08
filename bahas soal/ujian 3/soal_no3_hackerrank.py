class IncreasingList:
    def __init__(self):
        self.s = []

    def append(self, val):
        '''
        res = []
        for i in self.s:
            if i <= val
            res.append(i)
        self.s=res
        '''
        self.s = [i for i in self.s if i <= val]
        # self.s = list(filter(lambda x: x <= val, self.s))
        self.s.append(val)

    def pop(self):
        if len(self.s) > 0:
            self.s.pop()

    def __len__(self):
        return len(self.s)

if __name__ == '__main__':
    
    lst = IncreasingList()
    q = int(input())
    for _ in range(q):
        op = input().split()
        op_name = op[0] #append 3 
        if op_name == "append":
            val = int(op[1])
            lst.append(val)
        elif op_name == "pop":
            lst.pop()
        elif op_name == "size":
            print(len(lst))
        else:
            raise ValueError("invalid operation")

