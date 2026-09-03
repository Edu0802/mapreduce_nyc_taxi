from collections import defaultdict

def shuffle(nome_arquivo_entrada, nome_arquivo_saida):
    grupos = defaultdict(list)

    entrada = open(nome_arquivo_entrada, 'r', encoding='utf-8')

    for linha in entrada:
        if '\t' not in linha:
            continue

        chave, valor = linha.strip().split('\t')
        grupos[chave].append(int(valor))

    entrada.close()

    saida = open(nome_arquivo_saida, 'w', encoding='utf-8')
    saida.write(str(dict(grupos)))
    saida.close()

if __name__ == "__main__":
    shuffle("saida_mapper_q1.txt", "saida_shuffle_q1.txt")
