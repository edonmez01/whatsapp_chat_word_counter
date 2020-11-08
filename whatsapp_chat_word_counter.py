###############################################################
f = open(r"INPUT FILE LOCATION HERE", "r", encoding="utf-8")
out = open(r"OUTPUT FILE LOCATION HERE", "w", encoding="utf-8")
###############################################################

d = {}

while True:
    currentLine = f.readline()
    if not currentLine:
        break
    for i in range(2):
        if ":" not in currentLine:
            continue
        currentLine = currentLine[currentLine.index(":")+1:]

    currentList = currentLine.split()

    for j in currentList:
        j = j.lower()
        if j in ["<media", "omitted>"]:
            break
        while not j[-1].isalnum():
            j = j[:-1]
            if not j:
                break
        if not j:
            break
        if j not in d.keys():
            d[j] = 1
        else:
            d[j] += 1

d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

for i in d:
    out.write(str(i) + " " + str(d[i]) + "\n")
