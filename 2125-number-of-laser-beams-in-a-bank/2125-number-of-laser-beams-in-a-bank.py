class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows=len(bank)
        col=len(bank[0])
        res=0
        row1=0
        # Iterate through each row
        for i in range(rows):
            
            # Go over each col and get no.of 1's
            count1=0
            for j in range(col):
                if bank[i][j]=="1":
                    count1+=1   # Gives total no of 1's in row i
            if i==0:
                # Initail row, So No beams above it
                row1=count1
            else:
                if count1!=0:
                    res+=(row1*count1)
                    row1=count1
        return res
                
            
                
        