#input as array of tuples "arr" (instruction_string, value)[]


#PART 1:
height = 0
dist = 0
for inst in arr:
  if inst[0] == "forward":
    dist += inst[1]
  if inst[0] == "up":
    height -= inst[1]
  if inst[0] == "down":
    height += inst[1]

print(height*dist)


#PART 2:
height = 0
dist = 0
aim = 0
for inst in arr:
  if inst[0] == "forward":
    dist += inst[1]
    height += aim * inst[1]
  if inst[0] == "up":
    aim -= inst[1]
  if inst[0] == "down":
    aim += inst[1]

print(height*dist)
