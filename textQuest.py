def requireAnswerTwoDoors(whatFirstAnswerTwoDoors: str, whatSecondAnswerTwoDoors: str, firstAnswerTwoDoors: str, secondAnswerTwoDoors: str):
    answerInRequireTwoDoors = 0
    while True:
        answerInRequire = int(input(f"1 - {whatFirstAnswerTwoDoors} 2 - {whatSecondAnswerTwoDoors} \n"))
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
    answerInRequire = 0
    while True:
        answerInRequire = int(input(f"1 - {whatFirstAnswer} 2 - {whatSecondAnswer} \n"))
        if answerInRequire == 1:
            print(firstAnswer)
            break
        elif answerInRequire == 2:
            print(secondAnswer)
            break
        else:
            print("Неверный ответ")
    return answerInRequire


print("Вы открывая глаза, поняли что находитесь в комнате. Перед вами 2 двери. В какую войдёте?")

answer = requireAnswerTwoDooors("левая", "правая", "Вы выбрали левую.", "Вы выбрали правую.")


