# TPC2

## Enunciado
Completar um filtro que apaga linhas duplicadas de um ficheiro ou STDIN, com as opções:
- **-e** : remover linhas vazias
- **-p *str*** : comentar linhas duplicadas com *str* em vez de as apagar

## Funcionalidades
- Remover linhas duplicadas de um ficheiro de texto dado pelo utilizador;
- flag "-s" que permite manter os espaços em cada linha em vez de retirá-los;
- flag "-e" que permite remover as linhas vazias.
- flag "-p *str*" que permite comentar as linhas duplicadas com o caracter str ao invés de as apagar;
- > flag "-m *str*" que permite comentar as linhas vazias com str. *Não pode ser utilizada ao mesmo tempo que a flag "-e"*;
- > flag "-o *file*" que permite escrever o output no ficheiro *file*;
- > flag "-c" que permite obter no STDOUT o número de vezes que cada linha se repete, bem como em que linhas do ficheiro original estas estão. *Apenas pode ser utilizado se o input for um ficheiro*;
- > *as flags podem ser combinadas, salvo as exceções já mencionadas*.


## Comando

### Input no STDIN
```bash
python3 tpc2.py [opts]
```
ou
```bash
chmod +x tpc2.py \
./tpc2.py [opts]
```

### Input num ficheiro
```bash
python3 tpc2.py [opts] <file>
```
ou
```bash
chmod +x tpc2.py \
./tpc2.py [opts] <file>
```

