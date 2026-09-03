from collections import defaultdict

def shuffle(nome_arquivo_entrada, nome_arquivo_saida):
    grupos = defaultdict(list)

    entrada = open(nome_arquivo_entrada, 'r', encoding='utf-8')

    for linha in entrada:
        if '\t' not in linha:
            continue

        chave, valor_str = linha.strip().split('\t')
        try:
            distancia_str, pickup_datetime = valor_str.split(',')
            grupos[chave].append((float(distancia_str), pickup_datetime))
        except ValueError:
            continue

    entrada.close()

    saida = open(nome_arquivo_saida, 'w', encoding='utf-8')
    saida.write(str(dict(grupos)))
    saida.close()

if __name__ == "__main__":
    shuffle("saida_mapper_q4.txt", "saida_shuffle_q4.txt")
