import sys

files = []
opts = []

if sys.argv.__len__() >= 2:
    for arg in sys.argv:
        if arg[0] == "-":
            opts.append(arg)
        else:
            files.append(arg)
    
    if len(files) > 3:
        print("Invalid number of arguments     .")
        sys.exit()
    elif len(files) < 2:
        print("    Invalid number of arguments.")
        sys.exit()
else:
    print("Invalid number of arguments.")
    sys.exit()
    
f = open(files[1], "r")
fl = f.readlines()
f.close()

res = {}
for i in range(0, fl.__len__()):
    fl[i] = fl[i].split("\n")[0]
    if fl[i] in res.keys():
        res[fl[i]].append(i)
    else:
        res[fl[i]] = [i]
    

if "-c" in opts:
    print("----------------------------------------")
    for key, lineNrs in res.items():
        nrs = ""
        for ln in lineNrs:
            nrs += (", " if nrs != "" else "") + str(ln)
        print("The word '" + key + "' was written " + str(len(lineNrs)) + " time" + ("s" if (len(lineNrs) > 1) or (len(lineNrs) == 0) else ""))
        print("in the lines " + nrs)
        print("----------------------------------------")

if len(files) > 2:
    f = open(files[2], "w")
    for l in res.keys():
        f.write(l + "\n")
    f.close()
else:
    print("New file contents:")
    for l in res.keys():
        print(l)