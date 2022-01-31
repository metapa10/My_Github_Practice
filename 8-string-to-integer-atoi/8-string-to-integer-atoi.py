class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        i = 0
        n = len(s)
        
        int_max = pow(2,31) - 1
        int_min = -pow(2,31)
        
        while i < n and s[i] == ' ':
            i += 1
        if i < n and s[i] == '+':
            sign = 1
            i += 1
        elif i < n and s[i] =='-':
            sign = -1
            i += 1
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            if ((result > int_max // 10) or (result == int_max // 10 and digit > int_max % 10)):
                return int_max if sign == 1 else int_min
            
            result = 10 * result + digit 
            i += 1
            
        return sign * result 
        
        
        