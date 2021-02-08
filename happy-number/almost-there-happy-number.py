class Solution:
    def isHappy(self, n: int) -> bool:
        if n >= 1 or n <= ((2 ** 31) - 1):
            num = n
            squared_sum = ''
            while squared_sum != 1:
                num_list = []
                for i in str(num):
                    num_list.append(int(i))
                    squared_list = []
                    for k in num_list:
                        squared_list.append(k**2)
                squared_sum = sum(squared_list)
                num = sum(squared_list)
                print(num)
            return True
        else:
            return False
