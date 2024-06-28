import sys
def sort_student(students):
    count = 0
    for i in range(len(students)):
        for j in range(i+1, len(students)):
            if students[i] > students[j]:
                students[j],students[i] = students[i],students[j]
                count += 1
    return count

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    print(i+1, sort_student(list(map(int, sys.stdin.readline().split()))[1:]))