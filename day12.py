edges = [("FK","gc"),("gc","start"),("gc","dw"),("sp","FN"),("dw","end"),("FK","start"),("dw","gn"),("AN","gn"),("yh","gn"),("yh","start"),("sp","AN"),("ik","dw"),("FK","dw"),("end","sp"),("yh","FK"),("gc","gn"),("AN","end"),("dw","AN"),("gn","sp"),("gn","FK"),("sp","FK"),("yh","gc")]

def addNode(a, b, G):
    if(a not in G):
        G[a] = [b]
    else:
        G[a].append(b)

def genG():
    G = {}
    for e in edges:
        addNode(e[0], e[1], G)
        addNode(e[1], e[0], G)
    return G

def DFS(G, node, ban):
    sum = 0
    if (node == "end"):
        return 1
    newBan = ban.union(set())
    if (node.islower()):
        newBan = ban.union(set([node]))
    for n in G[node]:
        if(n not in ban):
            sum += DFS(G, n, newBan)
    return sum

def DFS2(G, node, ban, twice, tflag):
    sum = 0
    if (node == "end"):
        return 1
    newBan = ban.union(set())
    newTwice = twice.union(set())
    newtflag = tflag
    if (node.islower()):
        if(tflag or node in twice):
            newBan = ban.union(set([node])).union(twice) if not tflag else ban.union(set([node]))
            newtflag = True
        else:
            newTwice.add(node)
            
    for n in G[node]:
        if(n not in newBan):
            sum += DFS2(G, n, newBan, newTwice, newtflag)
    return sum

def part1():
    G = genG()
    sum = DFS(G, "start", set())
    print(sum)

def part2():
    G = genG()
    sum = DFS2(G, "start", set(["start"]), set(), False)
    print(sum)