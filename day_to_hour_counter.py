calculation_to_units = 24
name_of_unit = "godzin"


def days_to_units(num_of_days):
    return f"{num_of_days} dni to {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("wpisales 0, wpisz wartosc dodatnia :|")

    else:
        print("twoj wpis nie jest poprawna wartoscia, prosze nie psuj mi programu :)")


user_input = input("Siema uzytkowniku, wpisz liczbe dni a ja zamienie je na godziny!\n")
validate_and_execute()
