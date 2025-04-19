def lagrange(wezly, x):
    argumentyX = list(wezly.keys())

    for argument in argumentyX:
        if x == argument:
            return wezly[x]

    argumentyY = list(wezly.values())
    omega = 1

    for argument in argumentyX:
        omega *= (x - argument)

    funkcjeBazowe = []

    for indeks, argumentPodstawowy in enumerate(argumentyX):
        # inicjalizujemy daną funkcję 1, gdyż później dokonujemy mnożenia przez siebie
        funkcjeBazowe.append(1)
        for argumentOdjemnik in argumentyX:
            if argumentPodstawowy != argumentOdjemnik:
                funkcjeBazowe[indeks] *= (argumentPodstawowy - argumentOdjemnik)

    wynikSumy = 0.0
    for indeks, argumentPodstawowy in enumerate(argumentyX):
        # funkcjeBazowe[indeks] *= (x - argumentPodstawowy)
        wynikSumy += argumentyY[indeks] / (funkcjeBazowe[indeks] * (x - argumentPodstawowy))

    wynik = wynikSumy * omega

    return wynik