from num2words import num2words
from colorama import Style

summa = 0
while summa < 1 or summa > 100000:
    flag = 0
    # что бы проверить является ли введенная строка числом попробуем преобразовать ее в int и будем ловить исключение
    try:
        # Получаем введенное число суммы выдачи
        summa = int(input("Введите сумму выдачи: "))
    except ValueError:
        print("\033[31m", "Введенная cумма должна быть задана числом !!!" + Style.RESET_ALL)
        summa = 0
        flag = 1
        pass

    # Проверяем, что введенное число находится в диапазоне от 1 до 100000
    if flag == 0 and summa < 1 or summa > 100000:
        print("\033[31m", "Введенное число должно быть в диапазоне от 1 до 100000 !!!" + Style.RESET_ALL)

# Преобразуем число в слова с помощью num2words
summa_words = num2words(summa, lang='ru')

# Определяем правильное окончание для рублей
if summa % 10 == 1 and summa != 11:
    currency = "рубль"
elif summa % 10 in [2, 3, 4] and (summa % 100 < 10 or summa % 100 > 20):
    currency = "рубля"
else:
    currency = "рублей"

# Выводим результат
print(f"{summa_words.capitalize()} {currency}")
