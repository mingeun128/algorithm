n = int(input())
triangle = []
for i in range(n):
    temp = list(map(int, input().split()))
    triangle.append(temp)
for i in range(1,len(triangle)):
    for j in range(len(triangle[i])):
        if j<1:
            triangle[i][j]+=triangle[i-1][j]
        elif j == len(triangle[i])-1:
            triangle[i][j]+=triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
print(max(triangle[-1]))