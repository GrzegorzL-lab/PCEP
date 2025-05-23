# Slownik z wynikami uzytkownikow
wyniki = {
    "Anna": 15,
    "Bartek": 12,
    "Celina": 18
    }

# Zapytanie o imie uzytkownika
imie = input("Podaj swoje imie: ")

# Sprawdzenie, czy uzytkowni juz istnieje w slowniku
if imie in wyniki:
    print(f"Czesc, {imie}! Twoj poprzedni wynik to: {wyniki[imie]}")
else:
    print(f"Witaj, {imie}! Nie masz jeszcze zapisanego wyniku.")
    # Dodanie nowego uzytkownika z wynikiem 0
    wyniki[imie] = 0

# Aktualizacje wynikow
nowy_wynik = int(input("Podaj nowy wynik: "))
wyniki[imie] = nowy_wynik

print("\nAktualne wyniki:")
for gracz, wynik in wyniki.items():
  print(f"{gracz}: {wynik} punktow")
  
