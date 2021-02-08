class Solution:
    def isHappy(self, n: int) -> bool:
        num_list = []
        num = n
        squared_sum = ''
        while squared_sum != 1:
            for i in str(num):
                num_list.append(int(i))
                print(num_list)
                squared_list = []
                for k in num_list:
                    squared_list.append(k**2)
                    squared_sum = sum(squared_list)
