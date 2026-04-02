produto = {}
produto['nome'] = "Telemóvel"
produto['preço'] = 1500
produto['stock'] = 30
print(f"Lista inicial: {produto}")

del produto['stock'] 
print(f"Lista final: {produto}")
