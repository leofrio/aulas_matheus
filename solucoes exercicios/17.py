import math 

square_meters_qtd = float(input("diga a quantidade de m2 a serem pintados:")) 

redimento_litro = 6 
 
lata_litro = 18  
galao_litro = 3.6  
lata_preco = 80 
galao_preco = 25
lata_rendimento = lata_litro * redimento_litro 
galao_rendimento = galao_litro * redimento_litro 
apenas_lata = math.ceil(square_meters_qtd/lata_rendimento) 
apenas_lata_preco = apenas_lata * lata_preco
apenas_galao = math.ceil(square_meters_qtd/galao_rendimento)    
apenas_galao_preco=apenas_galao * galao_preco  

qtd_latas_both = math.floor(square_meters_qtd/lata_rendimento) 
qtd_galoes_both = math.ceil( (square_meters_qtd % lata_rendimento) / galao_rendimento) 
latas_preco_both = qtd_latas_both * lata_preco 
galao_preco_both = qtd_galoes_both * galao_preco 
print(f"apenas latas. qtd:{apenas_lata} preço: R$ {apenas_lata_preco}") 
print(f"apenas galoes qtd:{apenas_galao} preço: R$ {apenas_galao_preco}")  
print(f"os dois temos {qtd_latas_both} latas custando  R$ {latas_preco_both}\n e {qtd_galoes_both} galões  custando  R$ {galao_preco_both} \npara um perço total de R$ {galao_preco_both + latas_preco_both}")

# print(f"apenas galoes qtd:{apenas_galao} preço: R$ {apenas_galao_preco}") 



