class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            answers = [1,2]
            for i in range(2,n):
                answers.append(answers[i-1] + answers[i-2])
        return answers[-1]
