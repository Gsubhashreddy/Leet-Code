import random
class RandomizedSet:

    def __init__(self):
        self.di={}
        self.li=[]
        

    def insert(self, val: int) -> bool:
        if val in self.di:
            return False
        self.di[val] = len(self.li)
        self.li.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.di:
            return False
        idx,lastValue= self.di[val],self.li[-1]
        self.li[idx]=lastValue
        self.di[lastValue]=idx
        del self.di[val]
        self.li.pop()
        return True
    
    def getRandom(self) -> int:
        idx=random.randint(0,len(self.li)-1)
        return self.li[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()