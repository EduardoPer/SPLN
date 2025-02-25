import re
import jjcli
import collections

def lexer(txt):
    # FIXME patterns, stopwords, lems
    return re.findall(r'(\w+(?:\-\w+)*)|([^\w\s]+)', txt)

def counter(tokens):
    return collections.Counter(tokens)

def occurs_files(cl):
    counters = []
    countersp = []
    files = cl.args
    
    for txt in cl.text():
        l = lexer(txt)
        t,p = list(),list()
        for tup in l:
            if(tup[0] == ''):
                p.append(tup[1])
            else:
                t.append(tup[0])
        c = counter(t)
        cpun = counter(p)
        counters.append(c)
        countersp.append(cpun)
    
    if "-a" in cl.opt: #junta as frequencias asbsolutas de todos os ficheiros
        all = collections.Counter()
        allp = collections.Counter()
        
        for c in counters:
            all += c
        for c in countersp:
            allp += c
        
        print("Words:")    
        for (k, v) in all.items():
            print("\t" + str(k) + ": " + str(v))
        print("^Words:")
        for (k, v) in allp.items():
            print("\t" + str(k) + ": " + str(v))
            
    else: #frequencia absoluta por ficheiro
        for i in range(0, len(files)):
            print(files[i] + ":")
            print("\tWords:")
            for (k, v) in counters[i].items():
                print("\t\t" + str(k) + ": " + str(v))
            print("\t^Words:")
            for (k, v) in countersp[i].items():
                print("\t\t" + str(k) + ": " + str(v))

def occurs_stdin(cl):
    for txt in cl.input():
        l = lexer(txt)
        t,p = list(),list()
        for tup in l:
            if(tup[0] == ''):
                p.append(tup[1])
            else:
                t.append(tup[0])
        c = counter(t)
        cpun = counter(p)
        print("Words:")
        for (k, v) in c.items():
                print("\t\t" + str(k) + ": " + str(v))
        print("^Words:")
        for (k, v) in cpun.items():
                print("\t\t" + str(k) + ": " + str(v))

def main():
    cl = jjcli.clfilter(opt="a", man=__doc__)
    
    if len(cl.args) == 0:
        occurs_stdin(cl)
    else:
        occurs_files(cl)
