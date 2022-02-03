import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        big, small = [], []
        
        for num in range(1, int(math.sqrt(n)) + 1):
            if n % num == 0:
                if num == n // num:
                    small.append(num)
                else:
                        small.append(min(num, n // num))
                        big.append(max(num, n // num))
                        
        big.reverse()
        
        all_factors = small + big 
        
        if len(all_factors) >= k:
            return all_factors[k - 1]
       
        return -1