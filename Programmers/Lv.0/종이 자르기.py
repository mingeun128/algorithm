def solution(M, N):
    answer = (min(M,N)-1) + (max(N,M)-1) * min(N,M)
    return answer