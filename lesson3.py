x = input('Введите операцию +,-,/,*')

while x != '+' and x != '-' and x != '*' and x != '/':
    print('Ошибка! Такой операции не существует. Попробуйте еще раз.')
    x = input('Введите операцию: ')
y = int(input('Введите количество операндов: '))
a = float(input('Введите операнд 1: '))
result = a
c = str(a)

for i in range(2, y+1):
    a = float(input('Введите операнд ' + str(i) + ': '))
    if x == '+':
        result += a
    elif x == '-':
        result -= a
    elif x == '*':
        result *= a
    else:
        result /= a
    c = c + ' ' + x + ' ' +str(a)
c = c + ' = ' + str(result)
print(c)
