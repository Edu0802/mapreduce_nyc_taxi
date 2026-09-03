# MAPPER PARA QUESTÃO 5 — Quantidade de viagens por hora do dia

def map_viagens_por_hora(nome_arquivo_entrada, nome_arquivo_saida):
    entrada = open(nome_arquivo_entrada, 'r', encoding='utf-8')
    saida = open(nome_arquivo_saida, 'w', encoding='utf-8')

    # Descartar cabeçalho
    entrada.readline()

    for linha in entrada:
        campos = linha.strip().split(',')

        # Garantir coluna suficiente para acessar índice 1 (tpep_pickup_datetime)
        if len(campos) < 2:
            continue

        pickup_datetime = campos[1].strip()

        try:
            # O formato esperado é "YYYY-MM-DD HH:MM:SS"
            # Extrai a hora (substring das posições 11 a 13)
            partes_tempo = pickup_datetime.split(' ')
            if len(partes_tempo) >= 2:
                hora = partes_tempo[1].split(':')[0]
                if hora.isdigit():
                    saida.write(f"{hora}h\t1\n")
        except Exception:
            continue

    entrada.close()
    saida.close()

if __name__ == "__main__":
    map_viagens_por_hora("nyc_tripdata_2024_sample_1M.csv", "saida_mapper_q5.txt")
