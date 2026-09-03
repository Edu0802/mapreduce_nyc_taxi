# MAPPER PARA QUESTÃO 2 — Receita total por tipo de pagamento
payment_map = {
    '0': 'Flex Fare trip',
    '1': 'Credit card',
    '2': 'Cash',
    '3': 'No charge',
    '4': 'Dispute',
    '5': 'Unknown',
    '6': 'Voided trip'
}

def map_receita_por_pagamento(nome_arquivo_entrada, nome_arquivo_saida):
    entrada = open(nome_arquivo_entrada, 'r', encoding='utf-8')
    saida = open(nome_arquivo_saida, 'w', encoding='utf-8')

    # Descartar cabeçalho
    entrada.readline()

    for linha in entrada:
        campos = linha.strip().split(',')

        # Garantir colunas suficientes para acessar índice 16 (total_amount)
        if len(campos) < 17:
            continue

        codigo = campos[9].replace('.0', '')
        nome_pagamento = payment_map.get(codigo, 'Desconhecido')
        
        try:
            receita = float(campos[16])
            saida.write(f"{nome_pagamento}\t{receita}\n")
        except ValueError:
            continue

    entrada.close()
    saida.close()

if __name__ == "__main__":
    map_receita_por_pagamento("nyc_tripdata_2024_sample_1M.csv", "saida_mapper_q2.txt")
