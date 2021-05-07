class Solution(object):
    def isValid(self, s):
       
        stack = []
        dic = {")": "(", "}": "{", "]": "["}

        for char in s:           
            if char in dic:

                top_element = stack.pop() if stack else '#'
                if dic[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

# time and space O(n)        