import csv

path_do_arquivo = "vendas.csv"

def ler_arquivo(nome_arquivo_csv: str) -> list[dict]:
    """
    função que lê um arquivo em csv. e retorna em python
    de dicionarios
    """
    lista = []
    with open(nome_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista    

def filtrar_produtos_nao_entregues(lista: list) -> list[dict]:
    """
    função que filtra produtos onde entrega == True
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)        
    return lista_com_produtos_filtrados

def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    """
    função que soma todos os produtos que estão na lista
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
            valor_total += int(produto.get("price"))
    return valor_total

lista_de_produtos = ler_arquivo(path_do_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)
print(valor_dos_produtos_entregues)
