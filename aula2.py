# \r\n -> CRLF
# \n -> LF

# print possui o end='\n' por padrão
print(12, 34, 1011, sep="-", end='\r\n') # sep -> define o separador na linha / end -> o que executar no final da linha
print(56, 78, sep='-', end='## ')
print(9, 10, sep='-')