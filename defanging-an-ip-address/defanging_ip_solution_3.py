class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip = address
        defanged_ip = ''
        for i in ip:
            if i == ".":
                defanged_ip = defanged_ip+'[.]'
            else:
                defanged_ip = defanged_ip+i
        return defanged_ip
