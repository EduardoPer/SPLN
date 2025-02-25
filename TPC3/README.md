# TPC3

## Enunciado
Completar um script que calcula frequências de tokens num texto

## Funcionalidades
- Calcular frequência absoluta e/ou relativa de tokens em texto por STDIN
- Calcular frequência absoluta e/ou relativa de tokens em texto, dados um ou mais ficheiros
- Somar as frequências de tokens quando são dados vários ficheiros


## Comando
### Flags
- **"-a"**: frequências absolutas
- **"-m N"**: Limitar o output a N entradas
- **"-j FILENAME"**: criar um ficheiro Json com nome FILENAME que contém o counter unificado de todos os ficheiros
- **"-f"**: separar o output por ficheiros, dividindo em cada ficheiro por palavras e pontuação

### Instalar a ferramenta (dentro da pasta TPC3)
```bash
pip install .
```

### Desinstalar a ferramenta
```bash
pip uninstall ftk
```

### Calcular frequências no STDIN
```bash
ftk-occ
```

### Calcular frequências em ficheiros
```bash
ftk-occ [files] [opts]
```
