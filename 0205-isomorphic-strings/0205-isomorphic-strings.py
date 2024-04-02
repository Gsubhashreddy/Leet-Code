class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        fi={}
        se={}
        le = len(s)
        if le !=len(t):
            return False
        for i in range(le):
            if s[i] not in fi:
                if t[i] in se:
                    return False
                fi[s[i]] = t[i]
                se[t[i]]=True
            else:
                if t[i] not in se:
                    return False
                if t[i]!=fi[s[i]]:
                    return False
        return True