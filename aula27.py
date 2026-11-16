# 47. Fatiamento de strings e a função len

"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[:3])
print(variavel[-8:-2])
print(variavel[4:])
print(variavel[4:8])
print(len(variavel)) # contagem de CARACTERES, não índice
print(variavel[0:9:2]) # início : fim : passo (quantos caracteres pular)
print(variavel[0:9:-1]) # não executa, pois a contagem é negativa
print(variavel[-1:-10:-1]) # agora sim
print(variavel[::-1]) # de trás pra frente, de forma encurtada