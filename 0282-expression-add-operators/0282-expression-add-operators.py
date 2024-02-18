class Solution:
    res = []
    def evaluateExp(self, exp, target):
        ope = []
        opr = []
        i = 0
        num = ""
        while i <len(exp):
            if exp[i] == '+' or exp[i] =='-' or exp[i] == "*":
                if len(num) >1 and num[0] == "0":
                    # print("********")
                    return False
                ope.append(int(num))
                num = ''
                if opr and opr[-1] == '*':
                    a = ope.pop()
                    b = ope.pop()
                    opr.pop()
                    ope.append(a*b)
                opr.append(exp[i])
                
#             elif exp[i] == '*':
#                 ele1 = ope.pop()
#                 ele2 = int(exp[i+1])
#                 ele = ele1* ele2
#                 ope.append(ele)
#                 i +=1
            else:
                num += exp[i]
                # ope.append(int(exp[i]))
            i+=1
        if len(num) >1 and num[0] == "0":
            # print("********")
            return False
        ope.append(int(num))
        
        # print(exp, ope, opr)
        if opr and opr[-1] == "*":
            a = ope.pop()
            b = ope.pop()
            opr.pop()
            ope.append(a*b)
        while len(opr)!=0:
            expr = opr.pop(0)
            a = ope.pop(0)
            b = ope.pop(0)
            # print(a,b, expr)
            if expr == '+':
                ope.insert(0, a+b)
            elif expr == '-':
                ope.insert(0, a-b)
        # print(ope)
        # print(exp, ope[0])
        if ope[0] == target:
            print("************")
            return True
        return False
                
                
    
    def backTrack(self, nums, index, target, ops, res):
        #Base
        if index>= len(nums):
            temp = res[:]
            # print(temp)
            if self.evaluateExp(temp, target):
                self.res.append(temp)
            return
        
        # Logic
        for i in range(4):
            sym = ops[i]+nums[index]
            self.backTrack(nums, index+1, target, ops, res+sym)
            
            
    
    def addOperators(self, num: str, target: int) -> List[str]:
        self.res = []
        if len(num)==1:
            return []
        self.backTrack(num, 1, target, ['+', '-', '*',''], num[0])
        # self.evaluateExp("3-4+5+62*37*4-9-0", target)
        return self.res