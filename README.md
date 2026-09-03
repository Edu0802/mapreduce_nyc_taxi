# Análise de Dados de Viagens de Táxi de NY (1M de Registros) com MapReduce

Este repositório contém a implementação prática do paradigma **MapReduce** aplicada a uma base de dados com 1.000.000 de registros de viagens de táxis de Nova York (`nyc_tripdata_2024_sample_1M.csv`).

## 📌 Arquivos do Projeto

* `Trabalho_MapReduce_Eduardo_2412120032.ipynb`: Notebook Jupyter contendo a análise exploratória (EDA) e o fluxo de execução sequencial de todas as questões.
* `mapper_1.py` até `reducer_6.py`: Scripts modulares em Python contendo a lógica de processamento em três fases (`mapper`, `combiner` e `reducer`) para cada uma das 6 questões.

---

## ⚙️ Paradigma e Metodologia

O fluxo MapReduce foi implementado utilizando **Python Puro**, respeitando o pipeline de processamento distribuído/em lote:
1. **Mapper (`mapper_X.py`)**: Leitura sequencial das linhas, extração e filtragem dos campos necessários e emissão de pares `chave\tvalor`.
2. **Shuffle/Combiner (`combiner_X.py`)**: Agrupamento intermediário dos dados por chave usando `collections.defaultdict`.
3. **Reducer (`reducer_X.py`)**: Aplicação da função de agregação (`functools.reduce` e `ast.literal_eval`) e ordenação dos resultados finais.

---

## 📊 Resultados das Questões Práticas

### Questão 1: Quantidade de Viagens por Tipo de Pagamento
* **Credit card**: 743.405 viagens
* **Cash**: 136.221 viagens
* **Flex Fare trip**: 97.124 viagens
* **Dispute**: 16.543 viagens
* **No charge**: 6.707 viagens

### Questão 2: Receita Total por Tipo de Pagamento
* **Credit card**: $21.785.219,95
* **Cash**: $3.168.095,90
* **Flex Fare trip**: $2.376.069,77
* **No charge**: $53.932,48
* **Dispute**: $25.214,51

### Questão 3: Tarifa Média Geral Cobrada
* **Tarifa Média Geral**: $18,86

### Questão 4: Data e Hora da Viagem Mais Longa
* **Data/Hora**: `2024-05-10 17:33:00`
* **Distância**: 86.789,2 milhas *(Outlier identificado na amostragem)*

### Questão 5: Quantidade de Viagens por Hora do Dia
* **Pico de demanda**: 18h (71.403 viagens) e 17h (67.880 viagens)
* **Menor demanda**: 04h (6.054 viagens) e 05h (6.194 viagens)

### Questão 6: Distância Total Percorrida por Hora do Dia
* **Pico de quilometragem**: 17h (321.659,21 milhas) e 15h (312.374,38 milhas)
* **Menor quilometragem**: 04h (28.350,30 milhas) e 03h (29.745,90 milhas)

---

## 🚀 Como Executar

Para rodar a sequência de qualquer questão via terminal no Google Colab ou ambiente local:

```bash
python mapper_1.py
python combiner_1.py
python reducer_1.py
