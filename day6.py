fishes = [3,5,1,5,3,2,1,3,4,2,5,1,3,3,2,5,1,3,1,5,5,1,1,1,2,4,1,4,5,2,1,2,4,3,1,2,3,4,3,4,4,5,1,1,1,1,5,5,3,4,4,4,5,3,4,1,4,3,3,2,1,1,3,3,3,2,1,3,5,2,3,4,2,5,4,5,4,4,2,2,3,3,3,3,5,4,2,3,1,2,1,1,2,2,5,1,1,4,1,5,3,2,1,4,1,5,1,4,5,2,1,1,1,4,5,4,2,4,5,4,2,4,4,1,1,2,2,1,1,2,3,3,2,5,2,1,1,2,1,1,1,3,2,3,1,5,4,5,3,3,2,1,1,1,3,5,1,1,4,4,5,4,3,3,3,3,2,4,5,2,1,1,1,4,2,4,2,2,5,5,5,4,1,1,5,1,5,2,1,3,3,2,5,2,1,2,4,3,3,1,5,4,1,1,1,4,2,5,5,4,4,3,4,3,1,5,5,2,5,4,2,3,4,1,1,4,4,3,4,1,3,4,1,1,4,3,2,2,5,3,1,4,4,4,1,3,4,3,1,5,3,3,5,5,4,4,1,2,4,2,2,3,1,1,4,5,3,1,1,1,1,3,5,4,1,1,2,1,1,2,1,2,3,1,1,3,2,2,5,5,1,5,5,1,4,4,3,5,4,4]

def passDay(fishes):
    for f in range(len(fishes)):
        if(fishes[f] == 0):
            fishes[f] = 6
            fishes.append(8)
        else:
            fishes[f] -= 1

def passDay2(fishMap):
    newFishes = 0
    if(0 in fishMap):
        newFishes = fishMap[0]
    for i in range(9):
        if (i+1 in fishMap):
            fishMap[i] = fishMap[i+1]
        else:
            fishMap[i] = 0
    fishMap[8] = newFishes
    fishMap[6] += newFishes


def buildFishMap():
    fishMap = {}
    for f in fishes:
        if(f in fishMap):
            fishMap[f] += 1
        else:
            fishMap[f] = 1
    return fishMap

def part1():
    for i in range(80):
        passDay(fishes)
    print(len(fishes))

def part2():
    fishMap = buildFishMap()
    for day in range(256):
        passDay2(fishMap)

    count = 0
    for d in fishMap:
        count += fishMap[d]

    print(count)