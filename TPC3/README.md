# TPC3

## Enunciado
Completar um script que calcula frequências de tokens num texto

## Funcionalidades
- Calcular frequência absoluta de tokens em texto por STDIN
- Calcular frequência absoluta de tokens em texto, dados um ou mais ficheiros
- Somar as frequências de tokens quando são dados vários ficheiros


## Comando

### Instalar a ferramenta (dentro da pasta TPC3)
```bash
pip install .
```

### Desinstalar a ferramenta
```bash
pip uninstall ftk
```

### Calcular frequências absolutas no STDIN
```bash
ftk-occ
```

### Calcular frequências absolutas em ficheiros
```bash
ftk-occ [files]
```

### Calcular a soma das frequências absolutas em ficheiros
```bash
ftk-occ [files] -a
```
