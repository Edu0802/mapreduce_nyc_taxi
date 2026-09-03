from functools import reduce
import ast

def selecionar_maior(a, b):
    # Compara a distancia (a[0] vs b[0]) e mantem a tupla com a maior distancia
    return a if a[0] >= b[0] else b

def reducer(nome_arquivo_entrada, nome_arquivo_saida, funcao_reduce):
    entrada = open(nome_arquivo_entrada, 'r', encoding='utf-8')
    conteudo = entrada.read()
    entrada.close()

    dict_intermediario = ast.literal_eval(conteudo)

    resultado = {}
    for chave, lista_tuplas in dict_intermediario.items():
        maior_distancia, data_hora = reduce(funcao_reduce, lista_tuplas)
        resultado[chave] = (maior_distancia, data_hora)

    saida = open(nome_arquivo_saida, 'w', encoding='utf-8')

    for chave, (distancia, data_hora) in resultado.items():
        saida.write(f"Data e Hora da Viagem Mais Longa\t{data_hora}\t(Distância: {distancia} milhas)\n")

    saida.close()

if __name__ == "__main__":
    reducer("saida_shuffle_q4.txt", "saida_reduce_q4.txt", selecionar_maior)
