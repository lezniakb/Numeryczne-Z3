import math

def obliczWielomianHornerem(x, wspolczynniki):
    wynik = wspolczynniki[0]
    for wspolczynnik in wspolczynniki[1:]:
        wynik = wynik * x + wspolczynnik
    return wynik

# 2x - 3
def funkcjaLiniowa(x):
    return 2 * x - 3

# |x|
def funkcjaModul(x):
    return abs(x)

def funkcjaWielomianowa(x):
    wspolczynniki = [-2, 4, 0, 5] # odpowiada -2x^3 + 4x^2 + 5
    return obliczWielomianHornerem(x, wspolczynniki)

# sin(x) - 0.5
def funkcjaTrygonometryczna(x):
    return math.sin(x) - 0.5

# exp(sin(x)) - 2
def funkcjaZlozona(x):
    return math.e**(math.sin(x)) - 2