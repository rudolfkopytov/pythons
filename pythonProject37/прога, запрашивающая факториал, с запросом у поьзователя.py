#факториал - это сумма всех чисел от 1 до самого факториала
#n = int(input(' Введите число:'))
#fact_ =1
#for n in range(1, n + 1):
 #   fact_ = fact_ *  n
#print (" Факториал числа", n , "-", fact_)
# и ещё одно более простое решение - ф=вывода на экран факториала (суммы всех чисел в цифре)
n = int(input( ' Введите число'))
for number in range(1, n):
    n *= number
print(n)
