from desafio import ler_arquivo, filtrar_produtos_nao_entregues, somar_valores_dos_produtos

path_do_arquivo = "vendas.csv"


lista_de_produtos = ler_arquivo(path_do_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)
print(valor_dos_produtos_entregues)