def requireAnswerTwoDoors(whatFirstAnswerTwoDoors: str, whatSecondAnswerTwoDoors: str, firstAnswerTwoDoors: str, secondAnswerTwoDoors: str):
    answerBool = True
    answerInRequireTwoDoors = 0
    while answerBool:
        answerInRequire = int(input(f"1 - {whatFirstAnswerTwoDoors} 2 - {whatSecondAnswerTwoDoors} \n"))
        if answerInRequireTwoDoors == 1:
            answerBool = False
            print(firstAnswerTwoDoors)
        elif answerInRequireTwoDoors == 2:
            answerBool = False
            print(secondAnswerTwoDoors)
        else:
            print("Неверный ответ")
    return answerInRequireTwoDoors


print("Вы открывая глаза, поняли что находитесь в комнате. Перед вами 2 двери. В какую войдёте?")

answer = requireAnswerTwoDooors("левая", "правая", "Вы выбрали левую.", "Вы выбрали правую.")

def requireAnswerThreeDoors(whatFirstAnswerThreeDoors: str, whatSecondAnswerThreeDoors: str,whatThirdAnswerThreeDoors: str, firstAnswerThreeDoors: str, secondAnswerThreeDoors: str, thirdAnswerThreeDoors):
    answerBool = True
    answerInRequire = 0
    while answerBool:
        answerInRequire = int(input(f"1 - {whatFirstAnswer} 2 - {whatSecondAnswer} \n"))
        if answerInRequire == 1:
            answerBool = False
            print(firstAnswer)
        elif answerInRequire == 2:
            answerBool = False
            print(secondAnswer)
        else:
            print("Неверный ответ")
    return answerInRequire
