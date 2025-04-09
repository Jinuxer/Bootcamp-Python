saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando o saque!")
    print(f"Saldo em conta R$ {saldo - saque}")

#elif saldo < saque:
else:
    print("Saldo insuficiente")
    print(f"Você têm em conta R$ {saldo}")
