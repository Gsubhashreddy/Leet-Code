class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        di={}
        ti={}
        l1=len(s)
        l2=len(t)
        if l1!=l2:
            return False
        for i in range(l1):
            di[s[i]]=di.get(s[i],0)+1
            ti[t[i]]=ti.get(t[i],0)+1
        # print(di)
        # print(ti)
        if di==ti:
            return True
        return False
        for i in di:
            if di[i]!=ti[i]:
                return False
        return True