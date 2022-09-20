def requireAnswer(whatFirstAnswer: str, whatSecondAnswer: str, firstAnswer: str, secondAnswer: str):
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


print("Вы открывая глаза, поняли что находитесь в комнате. Перед вами 2 двери. В какую войдёте?")

answer = requireAnswer("левая", "правая", "Вы выбрали левую.", "Вы выбрали правую.")
