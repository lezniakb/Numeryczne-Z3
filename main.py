import os
import matplotlib.pyplot as plt
import numpy as np
import lagrange as l
import rownania as r

def wczytanie_wartosci(nazwa_pliku):
    # Otwieramy plik tylko do odczytu 'r'
    with open(nazwa_pliku, "r") as plik:
        # Tworzymy listę 'rownania', która zawiera wszystkie wiersze w pliku
        zawartosc = plik.read()
        wartosci = zawartosc.strip().split(',')

    return wartosci


def rysowanieFunkcji(funkcja, poczatek=-15.0, koniec=15.0):
    punktow = 400
    tablicaX = np.linspace(poczatek, koniec, punktow)
    tablicaY = []

    tablicaYlagrange = []

    for x in tablicaX:
        tablicaY.append(funkcja(x))
        tablicaYlagrange.append(l.lagrange(wezly, x))

    plt.figure(figsize=(8.2, 6.2))
    plt.plot(tablicaX, tablicaY, label="f(x)")
    plt.plot(tablicaX, tablicaYlagrange, label="g(x)")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)

    for wezel in wezly:
        plt.scatter(wezel, wezly[wezel], color="None", zorder=5,
                    marker="X", edgecolors="red", s=100)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Wykres funkcji")
    plt.legend()
    plt.grid(True)

    plt.show()


def zabezpieczenie(dane):
    # sprawdz czy podane dane sa floatem (liczba)
    if (dane.replace('.', '', 1).isdigit() or
            dane.lstrip('-').replace('.', '', 1).isdigit()):
        return True
    else:
        # jesli nie jest liczba, to zwroc stosowny komunikat
        print("Musisz podać liczbę!")
        return False


# main
funkcje = {
    1:("Liniowa: 2x - 3", r.funkcjaLiniowa),
    2:("Moduł: |x|", r.funkcjaModul),
    3:("Wielomianowa: -2x^3 + 4x^2 + 5 (Horner)", r.funkcjaWielomianowa),
    4:("Trygonometryczna: sin(x) - 0.5", r.funkcjaTrygonometryczna),
    5:("Złożona: exp(sin(x)) - 2", r.funkcjaZlozona)
}

nieIstnieje = None

petla = True

while True:
    # wybor funkcji przez uzytkownika
    print("Wybierz funkcje:")
    for wybor in funkcje:
        print(f"{wybor}: {funkcje[wybor][0]}")

    print("0. Zakończ program")

    wyborFunkcji = input("Podaj numer funkcji: ")
    dostepneWybory = [0, 1, 2, 3, 4, 5]

    if wyborFunkcji == "0":
        exit(0)

    # zabezpieczenie przez wprowadzaniem zlego znaku albo nieistniejacej funkcji
    # powtarzaj prosbe o podanie funkcji z zakresu
    while (wyborFunkcji.isdigit() == False) or (int(wyborFunkcji) not in dostepneWybory):
        print("Podaj liczbę całkowitą z przedziału 1-5!")
        wyborFunkcji = input("Podaj numer funkcji: ")

    # zapisz funkcje podana przez uzytkownika
    wyborFunkcji = int(wyborFunkcji)

    # zabezpieczenie przed podaniem niewlasciwego przedzialu
    poczatekPrzedzialu = input("Podaj początek przedziału: ")
    while zabezpieczenie(poczatekPrzedzialu) == False:
        poczatekPrzedzialu = input("Podaj początek przedziału: ")

    koniecPrzedzialu = input("Podaj koniec przedziału: ")
    while zabezpieczenie(koniecPrzedzialu) == False:
        koniecPrzedzialu = input("Podaj koniec przedziału: ")

    print("\n-------------\n"
          "Wybrana funkcja:", funkcje[wyborFunkcji][0],
          f"\nWybrany przedział: [{poczatekPrzedzialu}, {koniecPrzedzialu}]"
          f"\n-------------\n")

    # zapisz przedzialy jako float
    poczatekPrzedzialu = float(poczatekPrzedzialu)
    koniecPrzedzialu = float(koniecPrzedzialu)

    # zamien ze soba koniec i poczatek przedzialu, jezeli poczatek przedzialu jest dalej niz jego koniec
    if koniecPrzedzialu <= poczatekPrzedzialu:
        koniecPrzedzialu, poczatekPrzedzialu = poczatekPrzedzialu, koniecPrzedzialu

    funkcjaWybrana = funkcje[wyborFunkcji][1]

    print("-------------\n"
          "Podaj w jakiej formie chcesz podać wartości x węzłów\n"
          "1. Przez plik\n"
          "2. Przez teminal"
          f"\n-------------\n")
    wyborWezlow = int(input("Wybór(1/2): "))

    if wyborWezlow == 1:
        nazwaPliku = input("Podaj nazwe pliku: ")
        # nazwaPliku += ".txt"
        if not os.path.exists(nazwaPliku):
            print("Podany plik nie istnieje!")
            exit(1)
        wezlyX = wczytanie_wartosci(nazwaPliku)
    elif wyborWezlow == 2:
        # zapytanie do uzytkownika o podanie wezlow po przecinku
        wezlyX = input("Podaj po przecinku wartosci x węzłów (np. 1,2,3): ").split(",")
    else:
        print("Podano złą wartość!")
        exit(1)

    # utworz slownik na wezly
    wezly = {}

    # zapisz wartosci y odpowiadajace argumentom x
    for wezel in wezlyX:
        if float(wezel) <  poczatekPrzedzialu or float(wezel) > koniecPrzedzialu:
            print(f"węzeł {wezel} wychodzi poza zadany przedział, wartość zostaje pominięta!")
        else:
            wezly[float(wezel)] = float(funkcjaWybrana(float(wezel)))

    if not wezly:
        print("Podano brak węzłów!")
        exit(1)

    print("[Wyniki]\n------------------------------")

    rysowanieFunkcji(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu)