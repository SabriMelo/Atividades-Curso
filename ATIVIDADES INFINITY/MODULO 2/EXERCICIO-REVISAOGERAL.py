produto={}

for i in range(1, 6):
    name = input(f"Informe o nome do produto {i}: ")
    valor = float (input(f"Informe o valor do produto {i}: "))
    produto[name] = valor
    
total = 0
for valor in produto.values():
    total+=valor
    
print(f"\n O valor total dos produtos é: R$ {total:.2f}")        