# Задача 3. Вариант 38.
# Напишите программу, которая выводит имя "Юзеф Теодор Конрад Коженевский", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

# Kucheryavenko A. I.
# 17.03.2016

name = "Юзеф Теодор Конрад Коженевский"
print("Герой нашей сегодняшней программы - " + name)
alias = input("Под каким же именем мы знаем этого человека? Ваш ответ :")

print("Все верно: " + name + " - " + alias)

input("\n\nНажмите Enter для выхода.")