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
def human():
    myAnswers = ["Ano, jsem člověk", "Ale jo, snad jo :-)", "Občas si tím nejsem zcela jistý, zvlášť po víkendu", "No doufám, že ano :-)", "Ne, jsem robot"]
    if manOrWoman == True:
        print("Musím být člověk, jsem přeci " + gender)
    else:
        bestAnswer = random.randint(0,4)
        print(myAnswers[bestAnswer])
        

if answer == 1:
    time.sleep(6)
    human()
elif answer == 2:
    print(2)









# print(answer)
# print(type(answer))