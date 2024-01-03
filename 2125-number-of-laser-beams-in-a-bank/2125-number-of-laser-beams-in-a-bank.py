class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res=0
        row1=0
        col=len(bank[0])
        # Iterate through each row
        for i in range(col):
            if bank[0][i]=="1":
                row1+=1
        for i in range(1,len(bank)):            
            # Go over each col and get no.of 1's
            count1=0
            for j in range(col):
                if bank[i][j]=="1":
                    count1+=1   # Gives total no of 1's in row i
            if count1!=0:
                res+=(row1*count1)
                row1=count1
        return res
                
            
                
        