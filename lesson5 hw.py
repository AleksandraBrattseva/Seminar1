#                                                   ЗАДАЧА 1
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import randint
#
# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = 2021
# flag = randint(0,2)
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# def candiestake(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
#
#
# def total(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
#
# while value > 28:
#     if flag:
#         k = candiestake(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         total(player1, k, counter1, value)
#     else:
#         k = candiestake(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         total(player2, k, counter2, value)
#
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")



#                                                   ЗАДАЧА 2
# Создайте программу для игры в ""Крестики-нолики"".


print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)



#                                                   ЗАДАЧА 3
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


# with open('file.txt', 'r') as data:
#     mytext = data.read()
#
# def encode(ss):
#     code = ''
#     char = ''
#     count = 1
#     for i in ss:
#         if i != char:
#             if char:
#                 code += str(count) + char
#             count = 1
#             char = i
#         else:
#             count += 1
#     return code
# code = encode(mytext)
# print(code)
#
# with open('file2.txt', 'r') as data:
#     mytext2 = data.read()
#
# def decoding(ss: str):
#     count = ''
#     decode = ''
#     for char in ss:
#         if char.isdigit():
#             count += char
#         else:
#             decode += char * int(count)
#             count = ''
#     return decode
# decode = decoding(mytext2)
# print(decode)

