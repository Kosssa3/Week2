cena = float(input("Cena produktu: "))
ilosc = int(input("Ilość produktów: "))
cena_produktow = cena * ilosc
cena_z_przecena = cena_produktow * 0.85
print(f"Pełna Cena: ${cena_produktow:.2f}")
print(f"Cena po obiżce 15%: ${cena_z_przecena:.2f}")

