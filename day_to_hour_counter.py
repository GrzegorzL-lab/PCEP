calculation_to_units = 24
name_of_unit = "godzin"


def days_to_units(num_of_days):
    return f"{num_of_days} dni to {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        # chce wykonać zamiane tylko dla dodatnich wartosci
        # pamietac, że można zachować sobie kod używając znaku #
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("wpisales 0, wpisz wartosc dodatnia :(")
        else:
            print("wpisales ujemna wartosc, wpisz wartosc dodatnia :(")
    except ValueError:
        print("twoj wpis nie jest poprawna wartoscia, prosze nie psuj mi programu :)")


user_input = ""
while user_input != "exit":
    user_input = input("Siema uzytkowniku, wpisz liczbe dni po przecinkach, a ja zamienie je na godziny!\n")
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()
