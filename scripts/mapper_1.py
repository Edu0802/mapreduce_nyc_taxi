
# MAPPER PARA QUESTÃO 1 — Número de viagens por tipo de pagamento
payment_map = {
    '0': 'Flex Fare trip',
    '1': 'Credit card',
    '2': 'Cash',
    '3': 'No charge',
    '4': 'Dispute',
    '5': 'Unknown',
    '6': 'Voided trip'
}

def map_viagens_por_pagamento(nome_arquivo_entrada, nome_arquivo_saida):
    entrada = open(nome_arquivo_entrada, 'r', encoding='utf-8')
    saida = open(nome_arquivo_saida, 'w', encoding='utf-8')

    # Descartar cabeçalho
    entrada.readline()

    for linha in entrada:
        campos = linha.strip().split(',')

        # Garantir que a linha tem colunas suficientes
        if len(campos) < 10:
            continue

        codigo = campos[9].replace('.0', '')  # Remove decimais
        nome_pagamento = payment_map.get(codigo, 'Desconhecido')

        saida.write(f"{nome_pagamento}\t1\n")

    entrada.close()
    saida.close()

if __name__ == "__main__":
    map_viagens_por_pagamento("nyc_tripdata_2024_sample_1M.csv", "saida_mapper_q1.txt")
