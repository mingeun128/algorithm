def solution(numlist, n):
    answer = []
    distance = {}
    for i in numlist:
        if abs(n-i) not in distance:
            distance[abs(n-i)] = []
        distance[abs(n-i)].append(i)
    for i in distance:
        distance[i].sort()
    distance_keys = list(distance.keys())
    distance_keys.sort()
    for i in distance_keys:
        while len(distance[i]) > 0:
            answer.append(distance[i].pop())
    return answer