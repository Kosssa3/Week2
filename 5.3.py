liczba = 0

while True:
    total = float(input("Enter a number (0 to stop:) "))
    if total == 0:
        break
    liczba += total

print("Suma liczb: ", liczba)
