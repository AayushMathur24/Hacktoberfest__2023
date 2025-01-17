"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

 
Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'

"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if not(len(stack)):
                    return False
                last_ch = stack[-1]
                stack.pop()
                if (i == ')' and last_ch == '(') or (i == ']' and last_ch == '[') or (i == '}' and last_ch == '{'):
                    continue
                else:
                    return False

        return len(stack) == 0
        

sol = Solution()
ans = sol.isValid("()")
print(ans)

ans = sol.isValid("()[]{}")
print(ans)

ans = sol.isValid("(]")
print(ans)