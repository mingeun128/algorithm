import sys
n = int(sys.stdin.readline())
output_info = []
for i in range(n):
    output_info.append(sys.stdin.readline().rstrip().split())
for i in range(n):
    repeat_count = int(output_info[i][0])
    for j in range(len(output_info[i][1])):
        for k in range(repeat_count):
            print(output_info[i][1][j], end='')
    print()