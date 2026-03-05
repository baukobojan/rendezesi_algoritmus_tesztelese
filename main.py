import random


def buborek_rendezes(tomb_be):
    tomb = tomb_be.copy()
    n = len(tomb)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if tomb[j] > tomb[j + 1]:
                tomb[j], tomb[j + 1] = tomb[j + 1], tomb[j]

    return tomb


def general_veletlen_tomb(meret, felso_hatar):
    return [random.randint(0, felso_hatar) for _ in range(meret)]


if __name__ == "__main__":
    nyers_adat = general_veletlen_tomb(10, 100)
    print(f"Eredeti lista:  {nyers_adat}")

    rendezett = buborek_rendezes(nyers_adat)
    print(f"Rendezett lista: {rendezett}")
