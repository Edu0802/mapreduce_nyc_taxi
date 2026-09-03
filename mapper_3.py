# MAPPER PARA QUESTÃO 3 — Tarifa média cobrada nas viagens (Geral)

def map_tarifa_media(nome_arquivo_entrada, nome_arquivo_saida):
    entrada = open(nome_arquivo_entrada, 'r', encoding='utf-8')
    saida = open(nome_arquivo_saida, 'w', encoding='utf-8')

    # Descartar cabeçalho
    entrada.readline()

    for linha in entrada:
        campos = linha.strip().split(',')

        # Garantir colunas suficientes para acessar índice 10 (fare_amount)
        if len(campos) < 11:
            continue

        try:
            fare = float(campos[10])
            # Emite a chave única 'Geral' com o valor da tarifa e a contagem 1
            saida.write(f"Geral\t{fare},1\n")
        except ValueError:
            continue

    entrada.close()
    saida.close()

if __name__ == "__main__":
    map_tarifa_media("nyc_tripdata_2024_sample_1M.csv", "saida_mapper_q3.txt")
