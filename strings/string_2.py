nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Guilherme", "idade": 28}
saldo = 45.435
print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(nome, idade))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))

print("Nome: {nome} Idade: {idade}".format(**dados))

# F string versão mais nova usada!
print(30 * "-")
print("F string")
print(f"Nome: {nome} / Idade: {idade} / Saldo: {saldo:.2f}")
