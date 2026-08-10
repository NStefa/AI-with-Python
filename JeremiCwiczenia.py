'''
def oblicz_bmi(waga_kg, wzrost_m):
    bmi = waga_kg / (wzrost_m ** 2)
    if bmi <18.5:
        kategoria = "Niedowaga"
    elif bmi < 25:
        kategoria = "Norma"
    elif bmi >= 25 and bmi <= 30:
        kategoria = "Nadwaga"
    elif bmi >= 30:
        kategoria = "Otyłość"
    return bmi, kategoria

print(oblicz_bmi(70, 1.75))




koszyk = [
        ("jabłka", 3.99, 2),
        ("mleko", 2.49, 3),
        ("chleb", 5.99, 1),
        ("masło", 8.49, 1),
        ("jogurt", 1.99, 4),
    ]


def podsumowanie_koszyka(koszyk):


    ile = len(koszyk)
    najdrozszy = koszyk[0][0]
    najdrozszy_cena = koszyk[0][1]
    najtanszy = koszyk[0][0]
    najtanszy_cena = koszyk[0][1]
    suma = 0

    for nazwa,cena,ilosc in koszyk:
        suma += cena*ilosc
        if cena > najdrozszy_cena:
            najdrozszy = nazwa
            najdrozszy_cena = cena
        if cena < najtanszy_cena:
            najtanszy = nazwa
            najtanszy_cena = cena
    return {
        "liczba_produktow": ile,
        "najdroższy": najdrozszy,
        "najtańszy": najtanszy,
        "suma": suma
    }

print(podsumowanie_koszyka(koszyk))

ksiazka = {}


def dodaj_kontakt(ksiazka, imie, numer):
    if imie not in ksiazka:
        ksiazka[imie] = set()
    ksiazka[imie].add(numer)


def usun_numer(ksiazka, imie, numer):
    if imie in ksiazka:
        ksiazka[imie].discard(numer)


def wspolne_kontakty(ksiazka, imie1, imie2):
    if imie1 in ksiazka and imie2 in ksiazka:
        return ksiazka[imie1] & ksiazka[imie2]
    return set()


def wypisz_kontakty(ksiazka):
    for imie in sorted(ksiazka.keys()):
        print(imie, ":", ksiazka[imie])

        dodaj_kontakt(ksiazka, "Ania", "123-456-789")
        dodaj_kontakt(ksiazka, "Ania", "987-654-321")

        dodaj_kontakt(ksiazka, "Bartek", "123-456-789")
        dodaj_kontakt(ksiazka, "Bartek", "111-222-333")

        dodaj_kontakt(ksiazka, "Celina", "555-666-777")

        print("Wspólne numery Ania & Bartek:", wspolne_kontakty(ksiazka, "Ania", "Bartek"))

        print("\nWszystkie kontakty:")
        wypisz_kontakty(ksiazka)




'''
#=====================================================================================================
# zad 1
import pandas as pd
import numpy as np

przepisy = pd.read_csv("recipes.csv")

liczbaW = len(przepisy)
liczbaK = len(przepisy.columns)
print(liczbaK, liczbaW)

print(przepisy.head())

#print(przepisy.dtypes)


# zad 2
#ile jest róznych platform zamieniam na ile jiest różnych kategorii przepisów w mojej bazie
ileKategorii = przepisy['RecipeCategory'].nunique()
print("Ilosc kategorii: ", ileKategorii)



#zamiast gatunki, to jakie  kategorie występują w zbiorze
kategorie = przepisy['RecipeCategory'].unique()
print(kategorie)


#Które platformy mają najwięcej gier? -> Które kategorie mają najwięcej przepisów?
rankingKategorii = przepisy['RecipeCategory'].value_counts()
print(rankingKategorii.head(10))


#Jaka jest średnia i maksymalna sprzedaż globalna? -> średnia i maksymalna wartość dla kalorii
srednia = przepisy['Calories'].mean()
maksymalna = przepisy['Calories'].max()
print('srednia: ',srednia, 'maksymalna: ', maksymalna)




#zad 3
braki = przepisy.isna().sum()
print("braki: ", braki)  #cos dziwnego, chyba wczesniej wypisuje jak robię ctrl + F


najwiecej = braki.idxmax()
print("Najwiecej brakow ma: ", najwiecej)



kalorieNumpy = przepisy['Calories'].to_numpy()

sumaNp = np.nansum(kalorieNumpy)
sredniaNp = np.nanmean(kalorieNumpy) #nan bo jeśli jest nuill to wywali błąd

print("Suma kalorii (NumPy):", sumaNp)
print("Średnia kalorii (NumPy):", sredniaNp)





kalorie1000 = przepisy['Calories'] * 1000

print("\n Kalorie 1000:")
print(kalorie1000.head())