valor_1 = 2 
valor_2 = 6

valor_4 = 8
valor_5 = 1

def soma(valor_1_para_somar:float, valor_2_para_somar:float) -> float:
    """
    um função simples de soma de valores de tipo float, que retorna float
    """
    resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    return resultado_da_soma
    
valor_3 = soma(valor_1_para_somar=valor_1, valor_2_para_somar=valor_2)
valor_6 = soma(valor_4, valor_5)

print(valor_3)
print(valor_6)