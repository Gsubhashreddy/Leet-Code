class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        if len(v1)<= len(v2):
            for i in range(len(v1)):
                s1 = int(v1[i])
                s2 = int(v2[i])
                if s1 == s2:
                    continue
                elif s1 < s2:
                    return -1
                else:
                    return 1
            for j in range(i+1, len(v2)):
                tmp = int(v2[j])
                if tmp > 0:   
                    return -1
            return 0
        else:
            for i in range(len(v2)):
                s1 = int(v1[i])
                s2 = int(v2[i])
                if s1 == s2:
                    continue
                elif s1 < s2:
                    return -1
                else:
                    return 1
            for j in range(i+1, len(v1)):
                tmp = int(v1[j])
                if tmp > 0:   
                    return 1
            return 0
            