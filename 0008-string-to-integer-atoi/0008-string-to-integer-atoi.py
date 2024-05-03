class Solution:
    def myAtoi(self, s: str) -> int:
        ps = 2**31
        ne = -1*ps
        ps -= 1
        res = ""
        sign = True
        i = 0
        le = len(s)
        while i<le and s[i]== " ":
            i+=1
        if i<le and s[i] == "-":
            sign = False
            i+=1
        elif i<le and s[i] == "+":
            i+=1
        # print(s[i],tmp)
        while  i<le and ord(s[i])>= 48 and ord(s[i])<=57:
            # print(True)
            res+=s[i]
            i+=1
            # tmp = ord(s[i])
        if res == "":
            return 0
        if sign:
            res = int(res)
            if res > ps:
                return ps
            return res
        tmp = -1*int(res)
        if tmp < ne:
            return ne
        return tmp
        # return 0
        