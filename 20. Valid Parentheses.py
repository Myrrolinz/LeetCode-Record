class Solution:
    def isValid(self, s: str) -> bool:
        records = []
        for i in s:
            if i == '(':
                records.append(')')                
            elif i == '[':
                records.append(']')
            elif i == '{' :
                records.append('}')
            elif not records or records[-1] != i:
                return False
            else:
                records.pop()
                
        if not records:
            return True
        else:
            return False