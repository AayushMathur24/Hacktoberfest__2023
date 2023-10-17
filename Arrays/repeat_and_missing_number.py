"""
Repeat and Missing Number Array

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4

"""

class Solution:
    def repeatedNumber(self, A):
        # find length of list
        n = len(A)
        
        # find sum of integers from 1 to n 
        s_n = (n*(n+1))//2
        
        # find sum of squares of integers from 1 to n
        s2_n = (n * (n + 1) * ((2 * n) + 1)) // 6
        
        # calculate sum and sum of squares of given array
        s, s2 = 0,0
        for num in A:
            s += num
            s2 += num*num
                
        # s-s_n = a-b:
        num1 = s - s_n

        # s2-s2n = a^2-b^2:
        num2 = s2 - s2_n

        # Find a+b = (a^2-b^2)/(a-b):
        num2 = num2 // num1

        # Find a and b: a = ((a+b)+(a-b))/2 and b = a-(a-b),
        # Here, a-b = val1 and a+b = val2:
        a = (num1 + num2) // 2
        b = a - num1

        return [a, b]
    
sol = Solution()
ans = sol.repeatedNumber([3, 1, 2, 5, 3])
print(ans)