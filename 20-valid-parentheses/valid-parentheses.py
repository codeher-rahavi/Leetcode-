class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        for i in s:
            if i=='(':
                arr.append(')')
            elif i=='[':
                arr.append(']')
            elif i=='{':
                arr.append('}')
            else:
                if len(arr)==0 or i!=arr.pop():
                    return False
        
        return len(arr)==0
        
        
            
        