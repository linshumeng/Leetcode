class Solution:
    def isHappy(self, n: int) -> bool:

        def cal_sum(num):
            sum = 0
            while num:
                sum += (num % 10)**2
                num = num // 10
            return sum

        record = set()
        while True:
            print(n)
            n = cal_sum(n)
            print(n)
            if n == 1:
                return True
            elif n in record:
                return False
            else:
                record.add(n)


sol = Solution()
n = 19
print(sol.isHappy(n))
