class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''
        temp = []
        # counter for left and right brackets
        left = 0
        right = 0

        # s.length <= 2 then return empty string
        if len(s) <= 2:
            return ''

        for i in s:
            # first: append the i (bracket)
            temp.append(i)
            # counter
            if i == '(':
                left += 1
            else:
                right += 1
            # reset the counter, temp list and update res
            if left == right and left and right:
                res += ''.join(temp[1:len(temp)-1])
                left = 0
                right = 0
                temp = []
        return res
            