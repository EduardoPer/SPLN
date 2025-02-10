import sys

if sys.argv.__len__() == 2:
    fileIn = sys.argv[1]
elif sys.argv.__len__() == 3:
    fileIn = sys.argv[1]
    fileOut = sys.argv[2]
else:
    print("Invalid number of arguments.")
    sys.exit()
    
f = open(fileIn, "r")
fl = f.readlines()
f.close()

res = {}
for i in range(0, fl.__len__()):
    fl[i] = fl[i].split("\n")[0]
    if fl[i] in res.keys():
        res[fl[i]].append(i)
    else:
        res[fl[i]] = [i]
    
print("----------------------------------------")
for key, lineNrs in res.items():
    nrs = ""
    for ln in lineNrs:
        nrs += (", " if nrs != "" else "") + str(ln)
    print("The word '" + key + "' was written " + str(len(lineNrs)) + " time" + ("s" if (len(lineNrs) > 1) or (len(lineNrs) == 0) else ""))
    print("in the lines " + nrs)
    print("----------------------------------------")
    
if sys.argv.__len__() == 3:
    f = open(fileOut, "w")
    for l in res.keys():
        f.write(l + "\n")
    f.close()
else:
    print("New file contents:")
    for l in res.keys():
        print(l)