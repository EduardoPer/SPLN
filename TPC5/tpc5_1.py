import re
from lark import Lark, Transformer
import pandas as pd



grammar = r'''
start: (PAR_COM_PARENTESIS|pt_tt_line|pt_line|tt_line|FIG_LINE|UNKNOWN_LINE)*

pt_tt_line: pt_line tt_line

pt_line: PT_LINE UNKNOWN_LINE*
tt_line: TETUN_LINE UNKNOWN_LINE*

PAR_COM_PARENTESIS.2: /(\b\w+\b )+\(.+\)\s*\.+\s*\d+/

PT_LINE.3: /PORTUGUÊS: .*/
TETUN_LINE.3: /TETUN: .*/

FIG_LINE.3: /Figura\s*\d+\-.*\)/

UNKNOWN_LINE.1: /.+/


_NEWLINE.4: /\n+/
%ignore _NEWLINE
'''

text = r'''
Simplificação de Radicais (Simplifikasaun hosi Radikál sira).................................................. 118
Sinais (Sinál Sira) ...................................................................................................................... 119
Sistema (Sistema) ...................................................................................................................... 119
Subtração (Subtrasaun / Hasai / Kuran) .................................................................................... 119
Subtraendo (Subtraendu / Hamenus)......................................................................................... 119
Tangente (Tanjente) .................................................................................................................. 120
Tangram (Tangram) .................................................................................................................. 120
Teorema (Teorema) ................................................................................................................... 121
Termo (Termu) .......................................................................................................................... 121
Tetraedro (Tetraedru) ................................................................................................................ 121
Trapézio (Trapéziu) ................................................................................................................... 121
Triângulo (Triángulu)................................................................................................................ 122
Trigonometria (Trigonometria) ................................................................................................. 122
Unidade (Unidade) .................................................................................................................... 122
Valor Absoluto (Valór Absolutu) .............................................................................................. 122
Valor Médio (Valór Médiu) ...................................................................................................... 122
Variável (Variavel).................................................................................................................... 122


PORTUGUÊS: Localização de um ponto em relação ao eixo horizontal x. Pode ter
posição positiva, negativa ou nula. Exemplos: Ver em TETUN.
TETUN: Fatin ba pontu sira-ne´ebé iha relasaun ho eixu orizontál (eixu x). Bele iha
pozisaun pozitiva, negativa ka nula. Ezemplu sira:

Figura 1- Eixo X-Y com abscissas (Eixu X-Y ho absisa)
'''

test = r'''
Figura 1- Eixo X-Y com abscissas (Eixu X-Y ho absisa)
'''

class PT_TT(Transformer):
    def start(self, args):
        return args

    def pt_tt_line(self, args):
        return args
    
    def pt_line(self, args):
        ret = args[0]
        for i in range(1, len(args)):
            ret += " " + args[i]
        return ret
    
    def tt_line(self, args):
        ret = args[0]
        for i in range(1, len(args)):
            ret += " " + args[i]
        return ret
    
    def PAR_COM_PARENTESIS(self, t):
        a = re.split(r'\s*\(', t.value)
        b = re.split(r'\)', a[-1])
        return [a[0], b[0]]
    
    def PT_LINE(self, t):
        return re.split(r'\:\s*', t.value)[1]
    
    def TETUN_LINE(self, t):
        return re.split(r'\:\s*', t.value)[1]
    
    def FIG_LINE(self, t):
        par_pt_tt = re.split(r'^Figura\s*\d+\-\s*', t.value)[-1]
        a = re.split(r'\s*\(', par_pt_tt)
        b = re.split(r'\)', a[-1])
        return [a[0], b[0]]
    
    def UNKNOWN_LINE(self, t):
        return t.value

p = Lark(grammar, parser='lalr')
tree = p.parse(text)
pt = PT_TT()

pt_tt = pt.transform(tree)


print(pd.DataFrame(pt_tt))