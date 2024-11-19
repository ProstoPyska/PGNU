import random

def Vis():
  with open("слова.txt", "r", encoding="utf-8") as f:
    words = f.read().splitlines()

  word = random.choice(words)
  bukv = set(word)
  alf = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
  ugadani = set()
  ne_ugad = set()
  hp = 6

  # Начальный вывод
  print("Добро пожаловать в игру 'Виселица'!")
  print("Угадайте слово:",  len(word) * "_")

  # Основной цикл игры
  while hp > 0 and len(bukv) > 0:
    print("У вас осталось", hp, "жизней")
    print("Неугаданные буквы:", ' '.join(ne_ugad))
    guess = input("Введите букву: ").lower()

    if guess in alf - ne_ugad - ugadani:
      ugadani.add(guess)
      if guess in bukv:
        bukv.remove(guess)
        print(" ")
      else:
        ne_ugad.add(guess)
        hp -= 1
        print(" ")
    elif guess in ugadani:
      print("Вы уже угадали эту букву. Попробуйте другую.")
    else:
      print("Неверный ввод. Введите букву.")

    word_list = [letter if letter in ugadani else '_' for letter in word]
    print(" ".join(word_list))

  # Конец игры
  if len(bukv) == 0:
    print("Поздравляю! Вы угадали слово:", word)
  else:
    print("У вас закончились жизни. Слово было:", word)

Vis()