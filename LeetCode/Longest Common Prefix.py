class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        prefix = strs[0]
        for i in range(1,len(strs)):
            if strs[i] == '':
                return ''
            min_len = min(len(prefix),len(strs[i]))
            for j in range(min_len):
                if prefix[j] != strs[i][j]:
                    prefix = prefix[:j]
                    break
                if j == min_len-1:
                    prefix = prefix[:j+1]
        return prefix