class Solution:
    def removeDuplicates(self, s: str) -> str:
        records = []
        for i in s:
            if not records or records[-1] != i:
                records.append(i)
            else:
                records.pop()
        return ''.join(records)
