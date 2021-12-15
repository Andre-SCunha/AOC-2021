dMatrix = [[2,3,4,4,6,7,1,2,1,2,],[6,6,1,1,7,4,2,6,8,1],[5,5,7,5,5,7,5,5,7,3],[3,1,6,7,8,4,8,5,3,6],[1,3,5,3,8,2,7,3,1,1],[4,4,1,6,4,6,3,2,6,6],[2,6,2,4,7,6,1,6,1,5],[1,7,8,6,5,6,1,2,6,3],[3,6,2,2,6,4,3,2,1,5],[4,1,4,3,2,8,4,6,5,3]]

dir = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

def part1():
    sum = 0
    n = len(dMatrix)
    m = len(dMatrix[0])

    for step in range(100):
        stack = []
        for x in range(n):
            for y in range(m):
                dMatrix[x][y] += 1
                if(dMatrix[x][y] > 9):
                    sum += 1
                    dMatrix[x][y] = 0
                    stack.append((x,y))
        
        while(len(stack)):
            c = stack.pop()
            for d in dir:
                x = c[0] + d[0]
                y = c[1] + d[1]
                if(x >= 0 and x < n and y >= 0 and y < m):
                    if(dMatrix[x][y] != 0):
                        dMatrix[x][y] += 1
                        if(dMatrix[x][y] > 9):
                            sum += 1
                            dMatrix[x][y] = 0
                            stack.append((x,y))

    print(sum)

def part2():
    n = len(dMatrix)
    m = len(dMatrix[0])
    step = 1
    while True:
        sum = 0
        stack = []
        for x in range(n):
            for y in range(m):
                dMatrix[x][y] += 1
                if(dMatrix[x][y] > 9):
                    sum += 1
                    dMatrix[x][y] = 0
                    stack.append((x,y))
        
        while(len(stack)):
            c = stack.pop()
            for d in dir:
                x = c[0] + d[0]
                y = c[1] + d[1]
                if(x >= 0 and x < n and y >= 0 and y < m):
                    if(dMatrix[x][y] != 0):
                        dMatrix[x][y] += 1
                        if(dMatrix[x][y] > 9):
                            sum += 1
                            dMatrix[x][y] = 0
                            stack.append((x,y))
        if(sum == 100):
            print(step)
            return
        step += 1