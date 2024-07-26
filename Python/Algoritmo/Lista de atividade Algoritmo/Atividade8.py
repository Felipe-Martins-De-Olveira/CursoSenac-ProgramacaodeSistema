print("Digite uma distância em metros")
distancia_metros = float(input())
km = distancia_metros / 1000
hm = distancia_metros / 100
dm = distancia_metros * 10
cm = distancia_metros * 100
mm = distancia_metros * 1000  
print(f"A distância de {distancia_metros:}m corresponde a:")
print(f"{km:} Km")
print(f"{hm:} hm")
print(f"{dm:} dm")
print(f"{cm:} cm")
print(f"{mm:} mm")