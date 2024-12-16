def spela():
    print("Vad är värdet på x om x * 6 = 42?")
    gissning = int(input("Skriv in din gissning för x: "))

    if gissning == 7:
        print("Rätt svar!")
    else:
        if gissning > 7:
            print("Gissningen var för hög")
        else:
            print("Gissningen var för låg")
        print(f"Nej, {gissning} * 6 = {gissning * 6}.")

spela()