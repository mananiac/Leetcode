class Solution:
    def reverse(self, x: int) -> int:
        num=0
        c=abs(x)
        while (c is not 0):
            b = c %10
            c=c//10
            num = num*10+b
        if num.bit_length()>31:
            return 0
        elif x<0:
            return -1*num
        else:
            return num

# time O(log(n))
# space O(1)
