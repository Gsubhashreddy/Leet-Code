class Solution:
    def helper(self,s):
        di={}
        for i in s:
            di[i]=di.get(i,0)+1
        return di
    
    def minSteps(self, s: str, t: str) -> int:
        di={}
        res=0
        di1=self.helper(s)
        di2=self.helper(t)
        co1=0
        co2=0
        for i in di1:
            if di1[i]>1:
                co1+=di1[i]
        for i in di2:
            if di2[i]>1:
                co2+=di2[i]
        if co1<co2:
            #Pass
            temp=s
            s=t
            t=temp
            di=di2
        else:
            di=di1

        for i in t:
            if di.get(i,0)<=0:
                res+=1
            else:
                di[i] = di.get(i,0)-1
        return res
        