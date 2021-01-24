class Solution:
    def defangIPaddr(self, address: str) -> str:
        i = address.split('.')
            return '[.]'.join(i)
