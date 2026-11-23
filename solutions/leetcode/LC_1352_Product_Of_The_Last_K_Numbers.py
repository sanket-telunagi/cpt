# Solution for 1352. Product of the Last K Numbers
# Platform: LeetCode
# Date: 2026-11-23
#

class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0 :
            self.nums = [1]
            self.size = 0 
        else : 
            self.nums.append(self.nums[-1]*num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        return 0 if k > self.size else self.nums[self.size] // self.nums[self.size - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)



class ProductOfNumbers2:

    def __init__(self):
        self.stk = []
        

    def add(self, num: int) -> None:
        self.stk.append(num)
        # print(self.stk)

    def getProduct(self, k: int) -> int:
        res = 1
        # print(self.stk)
        # print(k,self.stk,self.stk[-(k):])
        temp = self.stk[-(k):]
        for num in temp : 
            res *= num
        return res


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
