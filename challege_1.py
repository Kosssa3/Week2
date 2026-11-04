numer = 14
próby = 0
max_prób = 5

while próby < max_prób:
    guess = int(input("Zgadnij numer: "))
    próby += 1

    if guess < numer:
        print("Za mało!")
    elif guess > numer:
        print("Za dużo!")
    else:
        print("Zdagłeś!")
        print(f"Zrobiłeś to w {próby} próbach.")
        break
else:
    print(f"Nie zgadłeś! Numerem było {numer}.")
