lista_passwords_validos = []
for i in range(11098, 98123):
    numero = str(i)
    if numero.count('5') > 1:
        if numero[0] <= numero[1] <= numero[2] <= numero[3] <= numero[4]:
            lista_passwords_validos.append(numero)

print(f"submit {len(lista_passwords_validos)}-{lista_passwords_validos[55]}")  # submit 165-23555
