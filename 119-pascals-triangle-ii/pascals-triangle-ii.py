class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        stack = []
        i = [0,1,0]
        a=sum(i)
        if rowIndex == 0:
            return [a]
        n=rowIndex
        while n>0:
            arr=[]
            for j in range(len(i)):
                s=sum(i[j:j+2])
                arr.append(s)
            
            c=arr[::-1]
            c.append(0)
            i=c
            n-=1
        return c[1:len(c)-1]