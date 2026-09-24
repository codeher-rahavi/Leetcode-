class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        stack = []
        initialize = [0,1,0]
        a = sum(initialize)
        stack.append([a])

        if numRows==1:
            return stack
        elif numRows>1:
            num = numRows
            while num>1:
                arr=[]
                for i in range(len(initialize)):
                    s= sum(initialize[i:i+2])
                    arr.append(s)
                c = arr[:len(arr)-1]
                stack.append(c)
                b=arr[::-1]
                b.append(0)
                initialize = b
                num-=1
        return stack
            

        