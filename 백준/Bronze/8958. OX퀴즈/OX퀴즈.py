num = int(input())


for j in range(num):
    dap = 0
    count = 0
    list = input()
    for i in range(len(list)):
        if list[i] == 'O':
            count = count + 1
        elif list[i] == 'X':
            count = 0

        dap = dap + count

    print(dap)