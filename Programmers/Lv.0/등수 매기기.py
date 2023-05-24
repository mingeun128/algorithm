def solution(score):
    n = len(score)
    answer = [0]*n
    avg_score = [((score[i][0]+score[i][1])/2,i) for i in range(n)]
    avg_score.sort(reverse = True)
    prev_score = avg_score[0][0]
    answer[avg_score[0][1]] = 1
    for i in range(1,n):
        if prev_score == avg_score[i][0]:
            answer[avg_score[i][1]] = answer[avg_score[i-1][1]]
        else:
            answer[avg_score[i][1]] = i+1
        prev_score = avg_score[i][0]
    return answer