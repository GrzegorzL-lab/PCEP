# wbudowane funkcje pythona uzyte ponizej
# print() - wyswietla zawartosc
# input() - pyta uzytkownika o wartosc
# set() - zaciąga listę i konwertuje w zbior
# int() - konwertuje wartosc w liczbe calkowita
# "2, 3".split() - rowniez wbudowana funkcja zaciągana bezpośredio do wartości
# Kazdy datatyp ma swoja pule funkcji, ktora mozna wykonac jak w #6
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} dni to {num_of_days * 24} godzin"
    elif conversion_unit == "minutes":
        return f"{num_of_days} dni to {num_of_days * 24 * 60} minut"
    else:
        return "niewspierana jednostka"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        # chce wykonać zamiane tylko dla dodatnich wartosci
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("wpisales 0, wpisz wartosc dodatnia :(")
        else:
            print("wpisales ujemna wartosc, wpisz wartosc dodatnia :(")
    except ValueError:
        print("twoj wpis nie jest poprawna wartoscia, prosze nie psuj mi programu :)")


user_input = ""
while user_input != "exit":
    user_input = input("Siema uzytkowniku, wpisz liczbe dni i jednostke konwersji (po angielsku) po dwukropku\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute()


# podsumowanie datatypow
# string - wiadomosc/wartosc typu "enter some value"
# integer - 20
# float number - 9.99
# boolean - sprawdzanie prawda/falsz np. valid_number = True / exit_input=False
# list - lista wartości w indeksowanej kolejności
#        list_of_days = [20, 40, 20, 100] / list_of_months = ["January, "February"]
# set - podobnie jak listy, ale nie pozwala na duplikaty wartosci i nie ma indeksowanej kolejności wartości
#       set_of_days = {20, 45, 100, 80}
# dictionary - zbiór kluczowych par wartości
#              days_and_unit = {"days": 10, "unit": "hours"}
