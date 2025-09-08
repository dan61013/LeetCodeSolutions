class Solution:
    def isValid(self, s: str) -> bool:
        # Empty Stack
        stack = []
        # mapping brackets
        match_dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        # if len(s) == 1 or s[0] in match_dict.values():
        #     return False
        # interate string
        for i in s:
            # append i when i equal (, [, {
            if i in match_dict.keys():
                stack.append(i)
                continue
            # pop i when meet right brackets
            if not stack:
                return False
            if i == match_dict[stack[-1]]:
                stack.pop(-1)
            else:
                return False
        # return stack, if empty stack means all the left brackets are matched and pop from stack
        return not stack