class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        long = list(s)
        short = list(t)
        if len(long) < len(short):
            long = list(t)
            short = list(s)
        for i in long:
            if i not in short:
                return False
            else:
                short.remove(i)
        return True