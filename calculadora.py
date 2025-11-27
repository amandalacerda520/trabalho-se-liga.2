#Criar função que calcula o total de uma compra (preço × quantidade).
#Envio:  Repositório com o programa e a Função funcionando no Python.




def calcular_total_item(preco: float, quantidade: int) -> float:
    """
    Calcula o valor total de um item: preço * quantidade.
    """
    return preco * quantidade

carrinho = [
    {'nome': 'Item Específico', 'preco': 5.99, 'quantidade': 4},
    {'nome': 'Lápis de Cor', 'preco': 12.50, 'quantidade': 3},
    {'nome': 'Bloco de Notas', 'preco': 8.00, 'quantidade': 1}
]

total_geral_compra = 0.0

print(" Cálculo Compra ")


for item in carrinho:
  
    preco_item = item['preco']
    quantidade_item = item['quantidade']
    
    
    total_item = calcular_total_item(preco_item, quantidade_item)
    
   
    total_geral_compra += total_item
    
    
    print(f"\nProduto: {item['nome']}")
    print(f"Cálculo: R$ {preco_item:.2f} x {quantidade_item} unidades")
    print(f"total: R$ {total_item:.2f}")
    print("-----------------------------------")

print(f"**TOTAL GERAL DA COMPRA: R$ {total_geral_compra:.2f}**")