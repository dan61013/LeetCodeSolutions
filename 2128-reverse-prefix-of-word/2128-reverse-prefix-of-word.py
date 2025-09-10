class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # return word while word length equal 1
        if len(word) == 1:
            return word
        # check whether find target character
        find_c = 0
        # counter the index for combine the result string(word)
        cnt = 0
        # save each reversed character
        rev_str = []
        for c in word:
            if c != ch:
                rev_str.insert(0, c)
                cnt += 1
                continue
            rev_str.insert(0, c)
            cnt += 1
            # check if 'ch' is exist in word
            find_c += 1
            break
        return ''.join(rev_str) + word[cnt:] if find_c else word