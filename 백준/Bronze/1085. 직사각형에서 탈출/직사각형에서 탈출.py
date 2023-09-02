positions = list(map(int, input().split()))
hansoo = [positions[0],positions[1]]
edge = [positions[2],positions[3]]
up = edge[1] - hansoo[1]
down = hansoo[1]
left = hansoo[0]
right = edge[0] - hansoo[0]
print(min(up,down,left,right))