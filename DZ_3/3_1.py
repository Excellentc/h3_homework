
def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    result_list = []
    for i in url_list:
        if "/catalog/" in i:
            result_list.append(i)
    return result_list


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    c = len(input_str )//2
    if len(input_str) % 2 == 0:
        output_str = input_str[c - 1: c + 1]
    else:
        output_str = input_str[c - 1: c + 2]
    return output_str


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    output_dict = {}
    input_str = input_str.replace(' ', '').lower()
    for i in input_str:
        x = input_str.count(i)
        output_dict[i] = x
    return output_dict


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    result_str = str1[0: len(str1 )//2] + str2 + str1[len(str1 )//2:]
    return result_str


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    x = [i for i in range(1, 100)]
    even_int_list = [i for i in x if i % 2 == 0]
    return even_int_list


us_inp = int(input("1. Find folder /catalog/ in url list - enter [1]\n"
                   "2. Returns X symbol from input Line - enter [2]\n"
                   "3. How many times does a letter appear in a string - enter [3]\n"
                   "4. Concatenating strings - enter [4]\n"
                   "5. Generating list from list - enter [5]\n"
                   ":"))
if us_inp == 1:
    z1 = int(input("Enter your url_list [1] or using my [2] ? :"))
    if z1 == 1:
        url_list_enter = input("Enter your url_list : ")
        print("Return url_list, with folder /catalog/", catalog_finder(url_list_enter))
    elif z1 == 2:
        url_list_enter = ["c:/asdf/asd/catalog/sefv.ed", "c:/asdf/asd/cat/sefv.ed",
                            "c:/asdf/asd/catalog/sev.ed", "c:/asdf/asd/cata/sefv.ed"]
        print("My list_url", url_list_enter)
        print("Return url_list, with folder /catalog/", catalog_finder(url_list_enter))
    else:
        print("You lose your choice, start anew this program")
elif us_inp == 2:
    input_str_enter = input("Enter your line : ")
    print("Return symbols from the middle of the line : ", get_str_center(input_str_enter))
elif us_inp == 3:
    inp_str = input("Input your line : ")
    print(count_symbols(inp_str))
elif us_inp == 4:
    str1_inp = input("Enter 1st line : ")
    str2_inp = input("Enter 2st line : ")
    print(mix_strings(str1_inp, str2_inp))
elif us_inp == 5:
    print(even_int_generator())
