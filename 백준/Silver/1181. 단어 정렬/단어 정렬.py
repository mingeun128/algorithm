n = int(input())
sens = []
for i in range(n):
    sens.append(input())
sens = list(set(sens))
sens = sorted(sens, key = lambda x : (len(x), x))
for i in range(len(sens)):
    print(sens[i])