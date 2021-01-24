class Solution:
    def defangIPaddr(self, address: str) -> str:
        i = address
        return i.replace('.', '[.]')
