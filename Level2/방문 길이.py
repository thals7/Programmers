# solution 1
def solution1(dirs):
    dir = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    limit = [6,-6]

    x,y = 0,0
    visited = []
    answer = 0

    for d in dirs:
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        if nx in limit or ny in limit:
            continue
        if (x,y,nx,ny) in visited:
            x,y = nx,ny
            continue
        visited.append((x,y,nx,ny))
        visited.append((nx,ny,x,y))
        x,y = nx,ny
        answer += 1

    return answer

# solution 2
def solution2(dirs):
    dir = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    limit = [6,-6]

    x,y = 0,0
    # visited를 중복 불가한 set로 두어 if 문 없이 바로 add 가능
    visited = set()

    for d in dirs:
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        if nx in limit or ny in limit:
            continue
        visited.add((x,y,nx,ny))
        visited.add((nx,ny,x,y))
        x,y = nx,ny

    # 매번 카운트 하지 않고 visited 길이/2 해서 경로수 구함
    return len(visited)//2