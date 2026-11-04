balans = 100.00

while True:
    print("\nATM Menu")
    print("1. Sprawdź balans")
    print("2. Depozyt")
    print("3. Wypłata")
    print("4. Wyjdź")

    choice = input("Wybierz opcje: ")

    if choice == "1":
        print(f"Balans wynosi: ${balans:.2f}")

    elif choice == "2":
        amount = float(input("Ilość depozytu: "))
        if amount > 0:
            balans += amount
            print(f"Depozyt zrobiony. Nowy balans: ${balans:.2f}")
        else:
            print("Ilość musi być większa niż 0.")

    elif choice == "3":
        amount = float(input("Ilość Wypłaty: "))
        if amount > 0 and amount <= balans:
            balans -= amount
            print(f"Wypłata zrobiona. Nowy balans: ${balans:.2f}")
        elif amount <= 0:
            print("Ilość musi być większa niż 0")
        else:
            print("Niewystarczające środki.")

    elif choice == "4":
        print("Do widzenia!")
        break

    else:
        print("Niemożliwa operacja. Proszę wybrać opcje 1, 2, 3, 4.")
