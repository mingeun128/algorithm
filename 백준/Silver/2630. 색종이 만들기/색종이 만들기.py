import sys
 
paper = []
blue = 0
white = 0
 
def sep_paper(start_x, end_x, start_y, end_y):
    global blue
    global white
    if start_x == end_x:
        if paper[start_y][start_x] == 0:
            white += 1
        else:
            blue += 1
        return
    color_sum = 0
    for i in range(start_y, end_y+1):
        color_sum += sum(paper[i][start_x:end_x+1])
    if color_sum == (end_x - start_x + 1)**2 or color_sum == 0:
        if color_sum == (end_x - start_x + 1)**2:
            blue += 1
        else:
            white += 1
        return
    else:
        sep_paper(start_x, (start_x + end_x) // 2, start_y, (start_y + end_y) // 2)
        sep_paper((start_x + end_x) // 2 + 1, end_x, start_y, (start_y + end_y) // 2)
        sep_paper(start_x, (start_x + end_x) // 2, (start_y + end_y) // 2 + 1, end_y)
        sep_paper((start_x + end_x) // 2 + 1, end_x, (start_y + end_y) // 2 + 1, end_y)
        return

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

sep_paper(0, n-1, 0, n-1)
print(white)
print(blue)