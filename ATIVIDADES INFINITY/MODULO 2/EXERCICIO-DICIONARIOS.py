contato = {}

nome = input("Digite o nome do contato: ")
telefone = input("Digite o número do contato: ")
email = input("Digite o email do contato: ")

contato["nome"] = nome
contato["telefone"] = telefone
contato["email"] = email

print("Informações do contato: ")
print(f"Nome: {contato["nome"]}")
print(f"Telefone: {contato["telefone"]}")
print(f"Email: {contato["email"]}")