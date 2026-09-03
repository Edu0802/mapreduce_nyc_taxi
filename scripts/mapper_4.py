# MAPPER PARA QUESTÃO 4 — Data e hora da viagem mais longa (trip_distance)

def map_viagem_mais_longa(nome_arquivo_entrada, nome_arquivo_saida):
    entrada = open(nome_arquivo_entrada, 'r', encoding='utf-8')
    saida = open(nome_arquivo_saida, 'w', encoding='utf-8')

    # Descartar cabeçalho
    entrada.readline()

    for linha in entrada:
        campos = linha.strip().split(',')

        # Garantir colunas suficientes para acessar índice 4 (trip_distance) e índice 1 (tpep_pickup_datetime)
        if len(campos) < 5:
            continue

        try:
            pickup_datetime = campos[1]
            distancia = float(campos[4])
            # Emite a chave 'Maior_Viagem' com a distancia e a data/hora de inicio
            saida.write(f"Maior_Viagem\t{distancia},{pickup_datetime}\n")
        except ValueError:
            continue

    entrada.close()
    saida.close()

if __name__ == "__main__":
    map_viagem_mais_longa("nyc_tripdata_2024_sample_1M.csv", "saida_mapper_q4.txt")
