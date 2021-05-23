calculation_to_units = 24
name_of_unit = "godzin"


def days_to_units(num_of_days):
    return f"{num_of_days} dni to {num_of_days * calculation_to_units} {name_of_unit}"

user_input = input("Siema uzytkowniku, wpisz liczbe dni a ja zamienie je na godziny!\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)