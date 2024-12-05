totDist = 0
f = open("input.txt", "r")
first = []
second = []

counter = 0
for x in f:
    values = x.split()
    firstval = values[0]
    secondval = values[1]
    first.append(firstval)
    second.append(secondval)
    counter = counter + 1

first.sort()
second.sort()

iterator = 0
while iterator < counter:
    comparator = 0
    whileFirst = 0
    whileSecond = 0
    whileFirst = int(first[iterator])
    whileSecond = int(second[iterator])
    print(iterator, " ", whileFirst, " ", whileSecond)

    if whileFirst > whileSecond:
        print ("first is bigger")
        comparator = whileFirst - whileSecond
    elif whileSecond > whileFirst:
        print ("second is bigger")
        comparator = whileSecond - whileFirst
    elif whileFirst == whileSecond:
        print ("match")
    totDist = totDist + comparator
    iterator = iterator + 1

# while first > 0 and second > 0:

#     print("comparator", comparator)
#     print("totDist ", totDist)
#     line = f.readline()
#     values = line.split()
#     first = int(values[0])
#     second = int(values[1])

print(totDist)
f.close()