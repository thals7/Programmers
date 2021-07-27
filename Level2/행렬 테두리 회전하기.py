def solution(rows, columns, queries):
    answer = []
    m = []
    for row in range(rows):
        m2 = []
        for column in range(1, columns + 1):
            m2.append(row * columns + column)
        m.append(m2)
    # List Comprehension 으로 행렬 생성
    # m = [[row*columns+column for column in range(1,columns+1)] for row in range(rows)]

    for query in queries:
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1

        start = m[x1][y1]
        minimum = start
        # Left
        for x in range(x1, x2):
            m[x][y1] = m[x + 1][y1]
            minimum = min(minimum, m[x][y1])
        # Bottom
        for y in range(y1, y2):
            m[x2][y] = m[x2][y + 1]
            minimum = min(minimum, m[x2][y])
        # Right
        for x in range(x2, x1, -1):  # 오른쪽
            m[x][y2] = m[x - 1][y2]
            minimum = min(minimum, m[x][y2])
        # Top
        for y in range(y2, y1, -1):  # 위쪽
            m[x1][y] = m[x1][y - 1]
            minimum = min(minimum, m[x1][y])
        m[x1][y1 + 1] = start

        answer.append(minimum)
    return answer