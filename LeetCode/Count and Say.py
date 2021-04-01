class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            prev_item = Solution.countAndSay(self,n-1)
            answer = ''
            count = 0
            pre_num = prev_item[0]
            for i in range(len(prev_item)):
                if pre_num == prev_item[i]:
                    count += 1
                else:
                    answer += str(count)
                    answer += pre_num
                    pre_num = prev_item[i]
                    count = 1
            answer += str(count)
            answer += pre_num
        return answer