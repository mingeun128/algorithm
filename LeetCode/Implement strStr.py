class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        nl = len(needle)
        hl = len(haystack)
        if nl>hl:
            return -1
        pi = [0]*nl
        j=0
        for i in range(1,nl): #get fail func
            while j>0 and needle[i]!=needle[j]:
                j=pi[j-1]
            if needle[i] == needle[j]:
                j+=1
                pi[i] = j
        k=0
        for i in range(hl):
            while(k>0 and haystack[i]!=needle[k]):
                k = pi[k-1]
            if haystack[i]==needle[k]:
                if k == nl-1:
                    return i-nl+1
                else:
                    k+=1
        return -1