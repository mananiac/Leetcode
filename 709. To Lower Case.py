class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()

class Solution2:
    def toLowerCase(self, str: str) -> str:
        l1 = ""
        for c in str:
            if "A" <= c <= "Z": 
                unicode = ord(c) + 32 
                char = chr (unicode) 
                l1 = l1+ char
            else:
                l1 = l1+ c

        return l1

# time O(n)
# space O (1)        