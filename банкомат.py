from num2words import num2words

# Получаем введенное число суммы выдачи
summa = int(input("Введите сумму выдачи: "))

# Проверяем, что введенное число находится в диапазоне от 1 до 100000
if summa < 1 or summa > 100000:
    print("Введенное число должно быть в диапазоне от 1 до 100000.")
else:
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
