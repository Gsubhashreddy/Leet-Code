class Solution:
    arrange = {}
    def arrange_num(self, num):
        co = 0
        if num in self.arrange:
            return self.arrange[num]
        for j in range(1,num +1):
            less_than = j-1
            greater_than = num-j
            # print(less_than,greater_than)
            # print(self.arrange)
            temp = self.arrange[less_than] * self.arrange[greater_than]
            co += temp
        self.arrange[num] = co


    def numTrees(self, n: int) -> int:
        self.arrange = {0:1, 1:1, 2:2}
        for i in range(1,n+1):
            self.arrange_num(i)
        return self.arrange[n]
            


        