while True:
    list_num = input()

    if list_num == '0':
        break

    if list_num == list_num[::-1]:
        print("yes")
    else:
        print("no")