# find the minimum number of flips required for "beautiful sequence"

flips = input('Enter a series of flips: ')
stringlength = len(flips)
flipstracker = []
for i in range(stringlength):
    hcount = 0
    tcount = 0
    for hcheck in range(stringlength - i):
        if flips[hcheck + i] == 'H':
            hcount = hcount + 1
    for tcheck in range(i):
        if flips[tcheck] == 'T':
            tcount = tcount + 1
    flipstracker.append(tcount + hcount)

minposition = 0
minflips = stringlength
for i in range(len(flipstracker)):
    if flipstracker[i] < minflips:
        minflips = flipstracker[i]
        minposition = i

print('The minimum number of flips is', minflips)
print('The transition from H to T happens at position', minposition)
