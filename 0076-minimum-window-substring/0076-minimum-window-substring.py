class Solution:
    def isEmpty(self,di):
        # print(di)
        for i in di:
            if di[i]>0:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        di ={}
        s.lower()
        t.lower()
        word = ""
        mini = float('inf')
        if len(t) > len(s):
            return ""
        for i in t:
            di[i]=di.get(i,0)+1
        st = 0
        curr = 0
        le = len(s)
        for cur in range(le):
            curr = s[cur]
            if curr in di:
                di[curr] -= 1
            if self.isEmpty(di):
                while st<= cur:
                    # print(st,cur)
                    temp = cur - st +1
                    if temp < mini:
                        mini =temp
                        word = s[st: cur+1]
                    mini = min(temp, mini)
                    val = s[st]
                    st += 1
                    if val in di:
                        di[val] += 1
                        if di[val] > 0:
                            break
                    
        return word
                
                  
            
        