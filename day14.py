import math

#poly = "NNCB"
#rules = [("CH","B"),("HH","N"),("CB","H"),("NH","C"),("HB","C"),("HC","B"),("HN","C"),("NN","C"),("BH","H"),("NC","B"),("NB","B"),("BN","B"),("BB","N"),("BC","B"),("CC","N"),("CN","C")]

poly = "VNVVKSNNFPBBBVSCVBBC"
rules = [("SV","C"),("SF","P"),("BP","V"),("HC","B"),("PK","B"),("NF","C"),("SN","N"),("PF","S"),("ON","S"),("FC","C"),("PN","P"),("SC","B"),("KS","V"),("OS","S"),("NC","C"),("VH","N"),("OH","C"),("BB","H"),("KV","V"),("HP","S"),("CP","H"),("SO","F"),("KK","N"),("OO","C"),("SH","O"),("PB","S"),("KP","H"),("OC","K"),("BN","F"),("HH","S"),("CH","B"),("PC","V"),("SB","N"),("KO","H"),("BH","B"),("SK","K"),("KF","S"),("NH","O"),("HN","V"),("VN","F"),("BC","V"),("VP","C"),("KN","H"),("PV","S"),("HB","V"),("VV","O"),("PO","B"),("FN","H"),("PP","B"),("BF","S"),("CB","S"),("NK","F"),("NO","B"),("CC","S"),("OF","C"),("HS","H"),("SP","C"),("VB","V"),("BK","S"),("CO","O"),("NS","K"),("PH","O"),("BV","B"),("CK","F"),("VC","S"),("HK","B"),("BO","K"),("HV","F"),("KC","V"),("CN","H"),("FS","V"),("VS","N"),("CF","K"),("VO","F"),("FH","H"),("NB","N"),("PS","P"),("OK","N"),("CV","O"),("CS","K"),("HO","C"),("KB","P"),("NN","V"),("KH","C"),("OB","V"),("BS","O"),("FB","H"),("FF","K"),("HF","P"),("FO","F"),("VF","F"),("OP","S"),("VK","K"),("OV","N"),("FK","H"),("FP","H"),("NV","H"),("NP","N"),("SS","C"),("FV","N")]

def applyRules():
    global poly
    ins = []
    for r in rules:
        mIns = []
        for i in range(len(poly)):
            if (poly[i:i+2] == r[0]):
                mIns.append((i+1, r[1]))
        ins.extend(mIns)

    ins.sort()
    carry = 0
    for i in ins:
        idx = i[0]+carry
        poly = poly[:idx] + i[1] + poly[idx:]
        carry += 1

def getMinMax():
    d = {}
    for c in poly:
        if (c not in d):
            d[c] = 1
        else:
            d[c] += 1

    max = 0
    min = math.inf
    for c in d:
        if(d[c] > max):
            max = d[c]
        elif(d[c] < min):
            min = d[c]

    return (max, min)

def part1():
    for _ in range(10):
        applyRules()
    max, min = getMinMax()
    print(max-min)

def buildPairDict():
    d = {}
    for i in range(len(poly)-1):
        pair = poly[i:i+2] 
        if(pair in d):
            d[pair] += 1
        else:
            d[pair] = 1
    return d

def updateDict(d):
    newPairs = []
    for r in rules:
        if (r[0] in d):
            fP = r[0][0] + r[1]
            sP = r[1] + r[0][1]
            v = d.pop(r[0])
            newPairs.append((fP, v))
            newPairs.append((sP, v))
    
    for pair,val in newPairs:
        if(pair in d):
            d[pair] += val
        else:
            d[pair] = val

def getMinMaxFromDict(d):
    cD = {}
    for pair in d:
        for c in pair:
            if (c not in cD):
                cD[c] = 0.5 * d[pair]
            else:
                cD[c] += 0.5 * d[pair]
    cD[poly[0]] += 0.5
    cD[poly[-1]] += 0.5

    max = 0
    min = math.inf
    for c in cD:
        if(cD[c] > max):
            max = cD[c]
        elif(cD[c] < min):
            min = cD[c]

    return (max, min)



def part2():
    d = buildPairDict()
    for _ in range(40):
        updateDict(d)
    max, min = getMinMaxFromDict(d)