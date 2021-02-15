class Solution:
    def isHappy(self, n: int) -> bool:
        seen_previously = dict()
        if n >= 1 or n <= ((2 ** 31) - 1):
            num = n
            squared_sum = ''
            while squared_sum != 1:
                if squared_sum in seen_previously:
                    return False
                # seen_previous = {5: True}
                # seen_previous = [5]
                seen_previously[squared_sum] = True
                # seen_previous = {5: True, 25: True} O(1)
                # seen_previous = [5, 25] O(n)
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
