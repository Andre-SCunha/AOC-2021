#input as array arr of strings

#PART 1:
res = [0,0,0,0,0,0,0,0,0,0,0,0]

for str in arr:
  for i in range(len(str)):
    if(str[i] == "1"):
      res[i] += 1

d = 1
gamma = 0
episilon = 0
for i in range(len(res)-1, -1, -1):
  if(res[i] >= len(arr)/2):
    gamma += d
  else:
    episilon += d
  d *= 2

print(episilon * gamma)

#PART 2:

epCom = 0
gaCom = 0

epArr = arr
gaArr = arr

for i in range(12):
  for str in gaArr:
    if(str[i] == "1"):
      gaCom += 1
  for str in epArr:
    if(str[i] == "1"):
      epCom += 1

  gaVal = 1 if gaCom >= len(gaArr)/2 else 0
  epVal = 0 if epCom >= len(epArr)/2 else 1

  gaCom = 0
  epCom = 0

  filGa = list(filter(lambda x: (int(x[i]) == gaVal), gaArr))
  if(len(filGa) == 0):
    gaArr = [gaArr[-1]]
  else:
    gaArr = filGa

  filEp = list(filter(lambda x: (int(x[i]) == epVal), epArr))
  if(len(filEp) == 0):
    epArr = [epArr[-1]]
  else:
    epArr = filEp

d = 1
gamma = 0
episilon = 0
for i in range(11, -1, -1):
  gamma += d if gaArr[0][i] == "1" else 0
  episilon += d if epArr[0][i] == "1" else 0
  d *= 2

print(episilon * gamma)
