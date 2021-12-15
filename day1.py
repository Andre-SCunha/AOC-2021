#input "arr" as array of nums

#PART 1:
last = None
count = 0
for h in arr:
  if (last != None and last < h):
    count += 1
  last = h

print(count)

#PART 2
count = 0
lastBeg = None

for i in range(len(arr)-2):
    if (lasBeg != None and lastBeg < arr[i+2]):
        count += 1
    lastBeg = arr[i]

print(count)