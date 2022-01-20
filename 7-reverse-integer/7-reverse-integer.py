class Solution:
    def reverse(self, x: int) -> int:
        reverse_number = 0
        Negative=False
        if x<0:
            Negative=True
            x = abs(x)
        while(x>0):
            digit=x%10
            reverse_number=reverse_number * 10 + digit
            x = x//10
        if reverse_number.bit_length()>=32:
            return 0
        if Negative:
            return 0-reverse_number
        return reverse_number