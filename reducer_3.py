from functools import reduce
import ast

def somar_tuplas(a, b):
    # Soma (soma_fare, soma_qtd)
    return (a[0] + b[0], a[1] + b[1])

def reducer(nome_arquivo_entrada, nome_arquivo_saida, funcao_reduce):
    entrada = open(nome_arquivo_entrada, 'r', encoding='utf-8')
    conteudo = entrada.read()
    entrada.close()

    dict_intermediario = ast.literal_eval(conteudo)

    resultado = {}
    for chave, lista_tuplas in dict_intermediario.items():
        total_fare, total_qtd = reduce(funcao_reduce, lista_tuplas)
        media = total_fare / total_qtd if total_qtd > 0 else 0.0
        resultado[chave] = round(media, 2)

    saida = open(nome_arquivo_saida, 'w', encoding='utf-8')

    for chave, media in resultado.items():
        saida.write(f"Tarifa Média Geral\t${media:,.2f}\n")

    saida.close()

if __name__ == "__main__":
    reducer("saida_shuffle_q3.txt", "saida_reduce_q3.txt", somar_tuplas)
