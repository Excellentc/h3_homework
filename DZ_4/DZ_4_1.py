def validate_password(password):
    """
    Функция принимает пароль строкой и выполняет валидацию с помощью трёх
    вспомогательных функций:
    1. Содержит только a−z, A−Z, 0−9
    2. Содержит четное количество букв
    3. Содержит нечетное количество цифр
    Основная функция возвращает True, если пароль валидный.
    Если пароль не валидный, возвращает лист стрингов, в которых перечислены
    причины неуспешной проверки. Например: ["содержит запрещенные символы"]
    """
    if valid_password_lett_numbe(password):
        if validate_letters_even(password):
            if validate_numbers_odd(password):
                return True
            else:
                print("Amounts of numbers not odd")
        else:
            print("Amounts of letters not even")
    else:
        print("You password have not correct symbols")
    pass


def valid_password_lett_numbe(password):
    if password.isalnum():
        return True
    else:
        return False


def validate_letters_even(input_str):
    buk_col = 0
    for item in input_str:
        if item.isalpha():
            buk_col += 1
    if buk_col % 2 == 0:
        return True
    else:
        return False


def validate_numbers_odd(input_str):
    num_count = 0
    for item in input_str:
        if item.isdigit():
            num_count += 1
    if num_count % 2 != 0:
        return True
    else:
        return False


password_user = input("Enter password : ")
print(validate_password(password_user))
