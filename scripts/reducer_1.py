from functools import reduce
import ast

def somar(x, y):
    return x + y

def reducer(nome_arquivo_entrada, nome_arquivo_saida, funcao_reduce):
    entrada = open(nome_arquivo_entrada, 'r', encoding='utf-8')
    conteudo = entrada.read()
    entrada.close()

    # Usar ast.literal_eval (seguro contra injeção de código)
    dict_intermediario = ast.literal_eval(conteudo)

    resultado = {}
    for chave, lista in dict_intermediario.items():
        resultado[chave] = reduce(funcao_reduce, lista)

    saida = open(nome_arquivo_saida, 'w', encoding='utf-8')

    # Ordenar do maior para o menor
    for chave in sorted(resultado, key=resultado.get, reverse=True):
        saida.write(f"{chave}\t{resultado[chave]}\n")

    saida.close()

if __name__ == "__main__":
    reducer("saida_shuffle_q1.txt", "saida_reduce_q1.txt", somar)
