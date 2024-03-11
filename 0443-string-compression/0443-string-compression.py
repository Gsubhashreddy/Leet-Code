from io import StringIO
class Solution:
    def compress(self, chars: List[str]) -> int:
        pre = chars[0]
        ind = 0
        co = 1
        for i in range(1, len(chars)):
            if chars[i] != chars[i-1]:
                if co ==1 :
                    chars[ind] = pre
                    ind+=1
                else:
                    co = str(co)
                    chars[ind] = pre
                    ind+=1
                    for j in co:
                        chars[ind] = j
                        ind+=1
                co = 1
                pre = chars[i]
            else:
                co += 1
        if co ==1 :
            chars[ind] = pre
            ind+=1
        else:
            co = str(co)
            chars[ind] = pre
            ind+=1
            for j in co:
                chars[ind] = j
                ind+=1
        return ind
                    
        