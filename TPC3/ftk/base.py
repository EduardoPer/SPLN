import re
import jjcli
import collections
import json

def lexer(txt):
    # FIXME patterns, stopwords, lems
    return re.findall(r'(\w+(?:\-\w+)*)|([^\w\s]+)', txt)

def counter(tokens):
    return collections.Counter(tokens)

def freqs(cl, all : collections.Counter, allp : collections.Counter, counters : list[collections.Counter], countersp : list[collections.Counter]):
    """
    -f              rel and abs freqs per file, separated by words and punctuation
    -a              abs freq
    -m 700          max 700 entries
    -j "filename"   one counter of all files tokens to a Json file named "filename"
    """
    
    all_allp = all + allp
    total_tokens = sum(all_allp.values())
    m = 0
    
    if "-m" in cl.opt:
        m = int(cl.opt.get("-m"))
        
    if "-j" in cl.opt:
        filename = cl.opt.get("-j")
        f = open(filename, "w")
        f.write(json.dumps(all_allp))
        f.close()
        
    if "-a" in cl.opt and "-f" in cl.opt:
        for i in range(0, len(cl.args)):
            j = 0
            jp = 0
            print(cl.args[i] + ":")
            print("\tWords:")
            for (k, v) in counters[i].items():
                if j >= m and m != 0:
                    pass
                else:
                    j+=1
                    print("\t\t" + str(k) + ": fa=" + str(v))
            print("\t~Words:")
            for (k, v) in countersp[i].items():
                if jp >= m and m != 0:
                    pass
                else:
                    jp+=1
                    print("\t\t" + str(k) + ": fa=" + str(v))
    
    elif "-a" in cl.opt:
        i = 0
        for (k, v) in all_allp.items():
            if i >= m and m != 0:
                pass
            else:
                i+=1
                print("\t" + str(k) + ": fa=" + str(v))
        
    elif "-f" in cl.opt:
        for i in range(0, len(cl.args)):
            print(cl.args[i] + ":")
            print("\tWords:")
            for (k, v) in counters[i].items():
                print("\t\t" + str(k) + ": fr=" + str(v/total_tokens))
            print("\t~Words:")
            for (k, v) in countersp[i].items():
                print("\t\t" + str(k) + ": fr=" + str(v/total_tokens))
    
    else:
        i = 0
        for (k, v) in all_allp.items():
            if i >= m and m != 0:
                pass
            else:
                i+=1
                print("\t" + str(k) + ": fr=" + str(v/total_tokens))
    

def occurs_files(cl):
    counters = []
    countersp = []
    
    ########## parse dos tokens ###########
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
        
    ######## soma dos counters para a soma de frequências absolutas ##############
    all = collections.Counter()
    allp = collections.Counter()
        
    for c in counters:
        all += c
    for c in countersp:
        allp += c
    ###############################################################################
    return all, allp, counters, countersp

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
        total_tokens = sum(c.values()) + sum(cpun.values())
        print("Words:")
        for (k, v) in c.items():
                print("\t\t" + str(k) + ": fa=" + str(v) + " ; fr=" + str(float(v/total_tokens)))
        print("~Words:")
        for (k, v) in cpun.items():
                print("\t\t" + str(k) + ": fa=" + str(v) + " ; fr=" + str(float(v/total_tokens)))

def main():
    cl = jjcli.clfilter(opt="afm:j:", man=__doc__)
    
    if len(cl.args) == 0:
        occurs_stdin(cl)
    else:
        all, allp, counters, countersp = occurs_files(cl)
        freqs(cl, all, allp, counters, countersp)
