import sys
n,m = map(int, sys.stdin.readline().split())
num_dogam = []
dict_dogam = {}
for i in range(n):
    pocketmon = sys.stdin.readline().rstrip()
    num_dogam.append(pocketmon)
    if pocketmon[0] not in dict_dogam:
        dict_dogam[pocketmon[0]] = []
    dict_dogam[pocketmon[0]].append((pocketmon,i+1))

for _ in range(m):
    quiz = sys.stdin.readline().rstrip()
    if ord(quiz[0]) > 47 and ord(quiz[0]) < 58:
        print(num_dogam[int(quiz)-1])
    else:
        for p in dict_dogam[quiz[0]]:
            if quiz == p[0]:
                print(p[1])
                break