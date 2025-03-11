import re
import jjcli
import collections
import json
from datetime import datetime

def lexer(txt):
    return re.findall(r'(\w+(?:\-\w+)*)|([^\w\s])', txt)

def counter(tokens):
    return collections.Counter(dict(collections.Counter(tokens).most_common()))

def freqs(cl, all : collections.Counter, allp : collections.Counter, counters : list[collections.Counter], countersp : list[collections.Counter]):
    """
    -f                  rel and abs freqs per file, separated by words and punctuation
    -a                  abs freq
    -m 700              max 700 entries
    -j "filename"       one counter of all files tokens to a Json file named "filename"
    -r corpus_filename  ratio with corpus_filename
    """
    
    all_allp = collections.Counter(dict((all + allp).most_common()))
    total_tokens = sum(all_allp.values())
    all_allp_filtered = dict(collections.Counter({k: v for k, v in all_allp.items() if v > 2}).most_common())
    all_allp_filtered_rel = dict(collections.Counter({k: (v/total_tokens) * 1000000 for k, v in all_allp.items() if v > 2}).most_common())
    m = 0
    
    if "-m" in cl.opt:
        m = int(cl.opt.get("-m"))
    
    elif "-j" in cl.opt and "-a" in cl.opt:
        filename = cl.opt.get("-j")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json.dumps(all_allp_filtered, ensure_ascii=False, indent=4))
    elif "-j" in cl.opt:
        filename = cl.opt.get("-j")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json.dumps(all_allp_filtered_rel, ensure_ascii=False, indent=4))
        
    elif "-a" in cl.opt and "-f" in cl.opt:
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
                print("\t\t" + str(k) + ": fr=" + str((v/total_tokens)*1000000))
            print("\t~Words:")
            for (k, v) in countersp[i].items():
                print("\t\t" + str(k) + ": fr=" + str((v/total_tokens)*1000000))
    
    else:
        i = 0
        for (k, v) in all_allp.items():
            if i >= m and m != 0:
                pass
            else:
                i+=1
                print("\t" + str(k) + ": fr=" + str((v/total_tokens)*1000000))
    

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
                print("\t\t" + str(k) + ": fa=" + str(v) + " ; fr=" + str(float(v/total_tokens)*1000000))
        print("~Words:")
        for (k, v) in cpun.items():
                print("\t\t" + str(k) + ": fa=" + str(v) + " ; fr=" + str(float(v/total_tokens)*1000000))
    
def ratio(cInput, cBase):
    ratio_dict = {}
    for k, v in cInput.items():
        ratio_dict[k] = v / cBase[k] if cBase.get(k) else 0
    return dict(collections.Counter(ratio_dict).most_common())

def corpus_to_dict(filename):
    corpus_dict = {}
    with open(filename, "r", encoding='utf-8') as f:
        text = f.read()
        tokens = re.findall(r'(\d+)\s+(.*)\n', text)
        for (v, k) in tokens:
            v = float(v)
            if v > 2:
                corpus_dict[k] = v
                
    return dict(collections.Counter(corpus_dict).most_common())

    

def main():
    cl = jjcli.clfilter(opt="afm:j:r", man=__doc__)
    
    if len(cl.args) == 0:
         occurs_stdin(cl)
    else:
        all, allp, counters, countersp = occurs_files(cl)
        freqs(cl, all, allp, counters, countersp)
        
def main_corpus():
    cl = jjcli.clfilter(opt="c:o:s:", man=__doc__)
    """
    -c corpus    corpus file with structure per line being 'Nocorr word'
    -o FILENAME  output ratio in json format to file FILENAME
    -s N         print the N words that are surprises
    """
    if "-c" in cl.opt:
        all, allp, _, _ = occurs_files(cl)
        all_allp = collections.Counter(dict((all + allp).most_common()))
        total_tokens = sum(all_allp.values())
        all_allp_filtered_rel = dict(collections.Counter({k: (v/total_tokens) * 1000000 for k, v in all_allp.items() if v > 2}).most_common())
        corpus_dict = corpus_to_dict(cl.opt.get("-c"))
        ratio_dict = ratio(all_allp_filtered_rel, corpus_dict)
        if "-o" in cl.opt:
            with open(cl.opt.get("-o"), "w", encoding="utf-8") as f:
                json.dump(ratio_dict, f, ensure_ascii=False, indent=4)
        else:
            with open(f"{datetime.now().timestamp()}.json", "w", encoding="utf-8") as f:
                json.dump(ratio_dict, f, ensure_ascii=False, indent=4)
        if "-s" in cl.opt:
            print(dict(collections.Counter(ratio_dict).most_common(int(cl.opt.get("-s")))))
