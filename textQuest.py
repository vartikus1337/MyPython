def requireAnswerTwoDoors(whatFirstAnswerTwoDoors: str, whatSecondAnswerTwoDoors: str, firstAnswerTwoDoors: str, secondAnswerTwoDoors: str):
    answerInRequireTwoDoors = 0
    while True:
        answerInRequireTwoDoors = int(input(f"1 - {whatFirstAnswerTwoDoors} 2 - {whatSecondAnswerTwoDoors} \n"))
        if answerInRequireTwoDoors == 1:
            print(firstAnswerTwoDoors)
            break
        elif answerInRequireTwoDoors == 2:
            print(secondAnswerTwoDoors)
            break
        else:
            print("Неверный ответ")
    return answerInRequireTwoDoors


def requireAnswerThreeDoors(whatFirstAnswerThreeDoors: str, whatSecondAnswerThreeDoors: str,whatThirdAnswerThreeDoors: str, firstAnswerThreeDoors: str, secondAnswerThreeDoors: str, thirdAnswerThreeDoors):
    answerInRequireTreeDoors = 0
    while True:
        answerInRequireThreeDoors = int(input(f"1 - {whatFirstAnswerThreeDoors} 2 - {whatSecondAnswerThreeDoors} 3 - {whatThirdAnswerThreeDoors} \n"))
        if answerInRequireThreeDoors == 1:
            print(firstAnswerThreeDoors)
            break
        elif answerInRequireThreeDoors == 2:
            print(secondAnswerThreeDoors)
            break
        elif answerInRequireThreeDoors == 3:
            print(thirdAnswerThreeDoors)
            break
        else:
            print("Неверный ответ")
    return answerInRequireThreeDoors



print("Вы открывая глаза, поняли что находитесь в комнате. Перед вами 2 двери. В какую войдёте?")

answer = requireAnswerTwoDoors("левая", "правая", "Вы выбрали левую.", "Вы выбрали правую.")

if answer == 1:
    print("Вы вошли в комнату \nДверь сзади захлоплулась \nВы почуствовали неприятный запах \nКомната была тёмная \nВы нащюпали  3 двери ")
    answer = requireAnswerThreeDoors("дверь от которой воняло", "Закрытая дверь","дверь, на которой вы нащюпали число 107...","При открытии этой двери вы зажали нос","Вы силой открыли дверь","При открытии двери вас затянуло туда нечто")
    if answer == 1:
        print("комната внутри была светлая и там были разложившиеся трупы \nдверь захлопнулась \nОНО хочет есть...")
    elif answer == 2:
        print("У вас болит рука \nПеред вами была очередь, в конце очереди был виден маленький источник света \nСпустя долгое время подошла ваша очередь \nПеред вами был стол, на котором была свечка\nЗа столом сидел препод\nПрепод спросил:'на тройку с натяжкой?'\nВы согласились\nПрепод говорит:'на натяжку' и гасит свечку...")
    else:
        print("Вы оказались за партой\nВам дали одинарный листок, на котором было написано ФИО преподавателя\nЭто был счастливый билет\nВы овтетили правильно и очутились дома...")
else:
    print("Вы зашли в хорошо освещённую комнату \nДверь захлопнулась \nВ ней были 2 дыры \nУ одной дыры была табличка, на которой написанно: 'бесконечная дыра приветствия мира'\nОт второй дыры воняло ")
    answer= requireAnswerTwoDoors("Дыра у которой была табличка","Дыра, от которой воняло","Вы прыгнули в дыру бесконечного приветствия мира","Вы прыгнули в вонючую дыру, вы почуствовали неприятный запах")
    if answer == 1:
        print("Вы будете бесконечно падать и приветствовать мир")
        while True:
                print("Hello World")
    else:
        print("Вы падали недолго\nВы приземлились на гору мусора\nВас встретили черепашки-ниндзя и увели куда-то\nНо куда и зачем история умалкивает...")
