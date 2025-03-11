# TPC4

## Enunciado
Completar um script que calcula frequências de tokens num texto com:
- filtrar palavras cuja freq abs seja <= 2
- comparar frequencias

## Funcionalidades
- Calcular frequência absoluta e/ou relativa de tokens em texto por STDIN
- Calcular frequência absoluta e/ou relativa de tokens em texto, dados um ou mais ficheiros
- Somar as frequências de tokens quando são dados vários ficheiros
- Exportar ficheiro json com o filtro do enunciado
- ratio de frequencias entre um ficheiro e um corpus


## Comando ftk-occ
### Flags
- **"-a"**: frequências absolutas
- **"-m N"**: Limitar o output a N entradas
- **"-j FILENAME"**: criar um ficheiro Json com nome FILENAME que contém o counter unificado de todos os ficheiros
- **"-f"**: separar o output por ficheiros, dividindo em cada ficheiro por palavras e pontuação

### Calcular frequências no STDIN
```bash
ftk-occ
```

### Calcular frequências em ficheiros
```bash
ftk-occ [files] [opts]
```

## Comando ftk-ratio-corpus
### Flags
- **"-c corpus"**    ficheiro corpus com a estrutura por linha sendo 'Nocorr word'
- **"-o FILENAME"**  output da razao em formato json para o ficheiro FILENAME
- **"-s N"**         print das N palavras que são mais surpresa

### Calcular frequências no STDIN
```bash
ftk-ratio-corpus file [opts]
```

## Instalar a ferramenta (dentro da pasta TPC4)
```bash
pip install .
```

## Desinstalar a ferramenta
```bash
pip uninstall ftk
```
