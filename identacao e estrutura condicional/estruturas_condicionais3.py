MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

# 1 método -----------------------
idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


# 2 método ---------------------

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")

else:
    print("Ainda não pode tirar a CNH.")


# 3 método -------------------------------

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")

else:
    print("Ainda não pode tirar a CNH.")
