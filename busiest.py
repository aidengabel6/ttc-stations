infile = open("stations-2017.csv")
totals = []
header = infile.readline()
for line in infile:
    line = line.removesuffix("\n")
    row = line.split(",")
    total = int(row[4])
    totals.append(total)
print("len of totals:", len(totals))
avg_totals = sum(totals)/len(totals)
print ("avg:", avg_totals)
