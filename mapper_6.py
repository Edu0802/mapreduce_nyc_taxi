# MAPPER PARA QUESTÃO 6 — Distância total percorrida por hora do dia

def map_distancia_por_hora(nome_arquivo_entrada, nome_arquivo_saida):
    entrada = open(nome_arquivo_entrada, 'r', encoding='utf-8')
    saida = open(nome_arquivo_saida, 'w', encoding='utf-8')

    # Descartar cabeçalho
    entrada.readline()

    for linha in entrada:
        campos = linha.strip().split(',')

        # Garantir colunas suficientes para acessar índice 1 (pickup) e índice 4 (trip_distance)
        if len(campos) < 5:
            continue

        pickup_datetime = campos[1].strip()

        try:
            distancia = float(campos[4])
            partes_tempo = pickup_datetime.split(' ')
            if len(partes_tempo) >= 2:
                hora = partes_tempo[1].split(':')[0]
                if hora.isdigit():
                    saida.write(f"{hora}h\t{distancia}\n")
        except ValueError:
            continue

    entrada.close()
    saida.close()

if __name__ == "__main__":
    map_distancia_por_hora("nyc_tripdata_2024_sample_1M.csv", "saida_mapper_q6.txt")
