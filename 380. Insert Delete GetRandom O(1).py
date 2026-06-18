import random

class RandomizedSet(object):
    
    def __init__(self):
        self.arr = []
        self.d = {}  
        
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            return False
        else:
            index=len(self.arr)
            self.arr.append(val)
            self.d[val]=index
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            index=self.d[val]
            l = self.arr[-1]
            self.arr[index] = l
            self.d[l] = index
            self.arr.pop()
            del self.d[val]

            return True

        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        if len(self.d)>0:
            return self.arr[random.randint(0,len(self.arr)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
val=2
param_1 = obj.insert(val)
param_2 = obj.remove(val)
param_1 = obj.insert(val)
param_3 = obj.getRandom()

print(param_1,param_2,param_3)
