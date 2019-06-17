from name_function import get_formated_name

while True:
    first_name=input("please input the first_name:")
    if first_name == 'q':
        break
    last_name=input("please input the last_name:")
    print(get_formated_name(first_name,last_name))