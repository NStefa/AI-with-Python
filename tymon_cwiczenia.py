def oblicz_bmi(waga_kg, wzrost_m):
    BMI = waga_kg/(wzrost_m**2)
    if waga_kg > 0 and wzrost_m > 0:
        if BMI < 18.5:
            kategoria = "Niedowaga"
        elif BMI >= 18.5 and BMI < 25:
            kategoria = "Norma"
        elif BMI >= 25 and BMI < 30:
            kategoria = "Nadwaga"
        else:
            kategoria = "Otyłość"

        return BMI, kategoria
    else:
        return 0


print("Ćwiczenie 1")
bmi, kat = oblicz_bmi(70, 1.75)
print(f"BMI = {bmi:.1f} ({kat})")



def podsumowanie_koszyka(koszyk):
    if not koszyk:
        return{
            "liczba_produktow": 0,
            "najdrozszy": None,
            "najtanszy": None,
            "suma": 0.0
        }


    suma = 0.0
    najtanszy_produkt = koszyk[0]
    najdrozszy_produkt = koszyk[0]


    for produkt in koszyk:
        nazwa, cena, ilosc = produkt
        if cena < najtanszy_produkt[1]:
            najtanszy_produkt = produkt

        if cena > najdrozszy_produkt[1]:
            najdrozszy_produkt = produkt
        suma += (cena*ilosc)



    return{
        "liczba_produktow": len(koszyk),
        "najdrozszy": najdrozszy_produkt[0],
        "najtanszy": najtanszy_produkt[0],
        "suma": suma
    }



koszyk = [
    ("jabłka", 3.99, 2),
    ("mleko", 2.49, 3),
    ("chleb", 5.99, 1),
    ("masło", 8.49, 1),
    ("jogurt", 1.99, 4),
]

print("\nĆwiczenie 2")
wynik = podsumowanie_koszyka(koszyk)
for k, v in wynik.items():
    print(f"{k}: {v}")




ksiazka = {}

def dodaj_kontakt(ksiazka, imie, numer):
    if imie not in ksiazka:
        ksiazka[imie] = set()
    ksiazka[imie].add(numer)

def usun_numer(ksiazka, imie, numer):
    if imie in ksiazka:
        ksiazka[imie].discard(numer)

def wspolne_kontakty(ksiazka, imie1, imie2):
    numery1 = ksiazka.get(imie1, set())
    numery2 = ksiazka.get(imie2, set())
    return numery1 & numery2

def wypisz_kontakty(ksiazka):
    for imie in ksiazka:
        print(f"{imie}: {ksiazka[imie]}")

dodaj_kontakt(ksiazka, "Ania", "123-456-789")
dodaj_kontakt(ksiazka, "Ania", "987-654-321")
dodaj_kontakt(ksiazka, "Bartek", "123-456-789")
dodaj_kontakt(ksiazka, "Bartek", "111-222-333")
dodaj_kontakt(ksiazka, "Celina", "555-666-777")

print("\nCwiczenie 3")
wypisz_kontakty(ksiazka)
usun_numer(ksiazka, "Bartek", '123-456-789')
print("------PO ZMIANIE------")
wypisz_kontakty(ksiazka)