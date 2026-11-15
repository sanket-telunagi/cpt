# Solution for 1524. Number of Sub-arrays With Odd Sum
# Platform: LeetCode
# Date: 2026-11-15
#

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7

        evens = 1
        odds = 0
        
        current_sum = 0
        res = 0
        
        for num in arr:
            current_sum += num
            
            if current_sum % 2 != 0:

                res = (res + evens) % MOD
                odds += 1
            else:
                res = (res + odds) % MOD
                evens += 1
                
        return res
        
        
class Solution2:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        res = 0
        for i in range(n) :
            odds = 0
            for j in range(i,n) :
                if arr[j] % 2 != 0 :
                    odds += 1
                if odds % 2 != 0 :
                    res += 1
        
        return res
