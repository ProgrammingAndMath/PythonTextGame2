
answer = input("Ты будешь играть? [да/нет] ")

if answer.lower().strip() == "да":

    answer = input("Вы достигаете перекрестка,вы хотите налево или направо? ")
    if answer == "налево":
        answer = input("Вы сталкиваетесь с монстром, вы хотите бежать или атаковать? ")

        if answer == "атаковать":
            print("Это была не лучшая идея, вы проиграли!")
            input()
        else:
            print("Хороший выбор, вы благополучно ушли.")

            answer = input("Вы видите машину и самолет. Что бы вы хотели взять? (машина/самолет) ")

            if answer == "самолет":
                print("К сожалению, вы не умеете летать... Игра окончена")
                input()
            else:
                print("Ты выиграл!")
                input()
    elif answer == "направо":
        print("Вы бесцельно идете вправо и падаете на клочок льда. У вас застряла нога и вы не можете продолжать игру!")
        print("Игра окончена!")
        input()
    else:
        print("Неверный выбор, вы проиграли!")
        input()
else:
    print("Это плохо")
    input()
