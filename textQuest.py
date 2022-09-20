def requireAnswer(whatFirstAnswer: str, whatSecondAnswer: str, firstAnswer: str, secondAnswer: str):
    answerInRequire = 0
    while answerBool:
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

answer = requireAnswer("левая", "правая", "Вы выбрали левую.", "Вы выбрали правую.")
