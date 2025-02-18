#!/usr/bin/env python3
'''
Repetidas - Remove linhas repetidas de um programa.

Usage - 
    ./tpc2.py options file*
    python3 tpc2.py options file*

Options - 
    -s              keep spaces
    -e              remove empty lines
    -p STR          comment duplicate lines with STR instead of removing them
    -m STR          comment empty lines with STR
    -o FILENAME     output the results in file named FILENAME
    -c              print the phrases' number of repetitions and lines in STDOUT
'''
from jjcli import *
import sys
linhas_vistas_count = dict()

#Usar flag para tirar espaços em branco, parágrafos...
def remove_linhas_repetidas(cl):
    linhas_vistas = set()
    lcount = 1
    for linha in cl.input():
        if "-s" in cl.opt: #keep spaces
            ln = linha
        else:
            ln = linha.strip()
            
        if not ln or ln not in linhas_vistas:
            if "-e" in cl.opt and not ln:
                pass
            elif "-m" in cl.opt and not ln:
                print(cl.opt.get("-m") + ln)
            elif not ln:
                print(ln)
            else:
                print(ln)
                linhas_vistas.add(ln)
                if ln in linhas_vistas_count.keys():
                    linhas_vistas_count[ln].append(lcount)
                else:
                    linhas_vistas_count[ln] = [lcount]
                
        elif ln in linhas_vistas:
            if ln in linhas_vistas_count.keys():
                    linhas_vistas_count[ln].append(lcount)
            else:
                linhas_vistas_count[ln] = [lcount]
                
            if "-p" in cl.opt:
                ln = cl.opt.get("-p") + linha
                print(ln)
        lcount += 1
        
def main():
    cl = clfilter(opt="sep:o:cm:", man=__doc__)
    
    if "-e" in cl.opt and "-m" in cl.opt:
        print("Can't use flags -e and -m at the same time.")
        sys.exit()
    if "-c" in cl.opt and cl.args == []:
        print("Can't use flag -c with input on STDIN.")
        sys.exit()
        
    original_stdout = sys.stdout
    if "-o" in cl.opt:
        sys.stdout = open(cl.opt.get("-o"), "w")
    remove_linhas_repetidas(cl)
    sys.stdout = original_stdout
    
    
    if "-c" in cl.opt:
        print("----------------------------------------")
        for key, lineNrs in linhas_vistas_count.items():
            nrs = ""
            for ln in lineNrs:
                nrs += (", " if nrs != "" else "") + str(ln)
            print("The phrase '" + key + "' was written " + str(len(lineNrs)) + " time" + ("s" if (len(lineNrs) > 1) or (len(lineNrs) == 0) else ""))
            print("in the lines " + nrs)
            print("----------------------------------------")
        
if __name__ == "__main__":
    main()
    
