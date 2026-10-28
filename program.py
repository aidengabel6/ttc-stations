infile = open("stations-2017.csv")
header = infile.readline()
totals = []
for line in infile:
    line = line.removesuffix('\n')
    row = line.split(",")
    total = int(row[4])
    totals.append(total)
infile.close()
avg_total = sum(totals) / len(totals)
print ("stations:", len(totals))
print ("average total:", avg_total)