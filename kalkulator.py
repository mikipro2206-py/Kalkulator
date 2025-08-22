print("")
print("Witaj w kalkulatorze stworzonym przez Mikołaja.K")
print("")

print("Instrukcja :")
print("1: Wpisz pierwszą liczbę i naciśnij klawisz ENTER.")
print("2: Wpisz drugą liczbę i ponownie naciśnij klawisz ENTER.")
print("3: Wybierz 1 z 7 znaków, które są opisane, i napisz ten znak, a następnie naciśnij ENTER.")
print("4: Pokaże się wynik, a następnie możesz wykonać kolejne działanie.")
print("5: Aby zakończyć program, po pokazaniu wyniku naciśnij tylko ENTER lub zamknij okno.")
print("")

while True:
    liczba_1 = float(input("liczba_1 :"))
    print("")
    liczba_2 = float(input("liczba_2 :"))
    print("")

    print(
        "Napisz znak + dodawanie lub - odejmowanie lub * mnożenie lub / dzielenie lub // dzielenie bez reszty lub % reszta z dzielenia lub ** potęga")
    print("")

    znak_1 = input("znak_1 :")
    print("")

    if znak_1 == "+":
        wynik = liczba_1 + liczba_2
    elif znak_1 == "-":
        wynik = liczba_1 - liczba_2
    elif znak_1 == "*":
        wynik = liczba_1 * liczba_2
    elif znak_1 == "/":
        if liczba_2 == 0:
            wynik = "Błąd: dzielenie przez zero"
        else:
            wynik = liczba_1 / liczba_2
    elif znak_1 == "//":
        if liczba_2 == 0:
            wynik = "Błąd: dzielenie przez zero"
        else:
            wynik = liczba_1 // liczba_2
    elif znak_1 == "%":
        if liczba_2 == 0:
            wynik = "Błąd: dzielenie przez zero"
        else:
            wynik = liczba_1 % liczba_2
    elif znak_1 == "**":
        wynik = liczba_1 ** liczba_2
    else:
        wynik = "Błąd: niepoprawny znak"

    print("Wynik to", wynik)
    print("")

    kontynuuj = input("Naciśnij Enter, aby zakończyć lub wpisz cokolwiek, aby zamknąć program: ")
    if kontynuuj == "":
        break
