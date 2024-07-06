value = int(input('Введите число от 3 до 20: '))
password = []

def getting_a_password(value):
    for i in range(1, 21):
        if i <= value:
            for j in range(1, 21):
                if j <= value:
                    if i >= j:
                        continue
                    if value % (i + j) == 0:
                        password.append(i)
                        password.append(j)
                else: break
        else:
            break
    print('Пароль: ', *password)

if 3 <= value <= 20:
    getting_a_password(value)
else:
    print('Введено некоректное значение')



