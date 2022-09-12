import random
import time
#definuju boolean jestli už se ptal na muže nebo ženu
manOrWoman = True
gender = "muž"
passedQuestion = []

print("Vítejte v obdobě Turingova testu")
print("Z 21 ti otázek jste si vybral/a 7 a ty mi můžete pokládat v jakémkoliv pořadí")

answer = int(input("Dobrý den, nyní se můžete ptát."))
# kdyz se predtim zepta jestli jsem muz nebo zena, tak napisu, kdyj jsem zena, jsem preci take clovek
# osetrit ze se zepta dvakrat na stejnou otazku


def weather_21():
    answers=["Dobrý den, venku vypadá krásně. Takže určitě bude sluníčko. Ptejte se dál! Ráda bych vám pomohla :)",
      "Dobrý den, vidím na nebi jsou černé mraky, zatím nebude pršet, ale až odpoledne určitě bude",
      "BUDE BOUŘKA!",
      "Prosím pokud jdete ven, tak vemte s sebou i deštník nebo pláštěnku. Bude dnes pršet, možná přijde i bouřka"]

    for x in range(1):
        resp=random.choice(answers)
    print(resp)


def human_1():
    myAnswers = ["Ano, jsem člověk", "Ale jo, snad jo :-)", "Občas si tím nejsem zcela jistý, zvlášť po víkendu", "No doufám, že ano :-)", "Ne, jsem robot"]
    if manOrWoman == True:
        print("Musím být člověk, jsem přeci " + gender)
    else:
        bestAnswer = random.randint(0,4)
        print(myAnswers[bestAnswer])
        

if answer == 1:
    time.sleep(1)
    human_1()
elif answer == 21:
    time.sleep(1)
    weather_21()









# print(answer)
# print(type(answer))