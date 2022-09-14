import random
import time
#definuju boolean jestli už se ptal na muže nebo ženu
manOrWoman = True
gender = "muž"
passedQuestion = []

print("Vítejte v obdobě Turingova testu")
print("Z 21 ti otázek jste si vybral/a 7 a ty mi můžete pokládat v jakémkoliv pořadí")

firstAnswer = ["S čím vám mohu pomoci?", "Tak se ptejte", "Tak poslouchám"]
answers = ["Máte další otázku?", "Co by vás dále zajímalo?", "Můžete se ptát dál", "A dál?", "Ještě něco?"]
lastAnswer = "Máte poslední otázku"

fa = random.choice(firstAnswer)

answer = int(input(fa))
# kdyz se predtim zepta jestli jsem muz nebo zena, tak napisu, kdyj jsem zena, jsem preci take clovek
# osetrit ze se zepta dvakrat na stejnou otazku

#
def lunch_4():
    answers = ["Dneska jsem si dal k obědu kebab","Oběd jsem dneska ještě neměl","Oběd si dám až později"]
    for x in range(1):
     resp=random.choice(answers)
     print(resp)
#
def matika_6():
    a = random.randrange(1, 10)
    if a == 1:
        time.sleep(3)
        print("To zpaměti nedam")
        time.sleep(5)
        print("Mělo by to být 20385")
    elif a == 2:
        time.sleep(2)
        print("Matika nee")
        time.sleep(5)
        print("Podle kalkulačky je to 20 385")
    elif a == 3:
        time.sleep(2)
        print("To nevypočitam")
    elif a == 4:
        time.sleep(7)
        print("20385")
    elif a == 5:
        time.sleep(6)
        print("20 385")
    elif a == 6:
        time.sleep(2)
        print("To je snadný")
        time.sleep(5)
        print("Je to 19 932")
    elif a == 7:
        time.sleep(2)
        print("Tak to netuším")
    elif a == 8:
        time.sleep(4)
        print("Nechci matiku. To nebudu počítat")
    elif a == 9:
        time.sleep(10)
        print("Myslím že to je 20385")
    else:
        time.sleep(5)
        print("Určitě to je 20 385")
#
def movies_7():
    answers=["Včera dávaly pořad Game of Thrones","Včera nedávali nic zajímavého","Včera měl být film Zelená míle, avšak pustili ho pozdě.","Nevím","Nedívám se na televizi"]
    for x in range(1):
        resp=random.choice(answers)
    print(resp)
#
def Kenobi_20():
    obi = ['Obivan Kenobi je hlavní postava z filmu StarWars.', 'Obi-Wan Kenobi je fiktivní postava ze Star Wars, jedna z ústředních postav celé ságy.', 'Nevím asi nějaká postava z filmu.']
    rndobi = random.choice(obi)
    print(rndobi)
#
def Siblings_17():
    odpovedi_17 = ["Co to je za blbo0u otázku? Samozřejmě že ano!", "... Dej mi chvilku.", "Ano", "Jo, asi ano.", "Nemám, protože jsem počítač.", "1101110 1100101 1101101 111111 111111", "Mám sourozence. Mám jednoho bratra a jednu sestru."]
    
    for x in range(1):
        ans = random.choice(odpovedi_17)
    if ans == odpovedi_17[1]:
        odpovedi_17.remove(odpovedi_17[1])
        ans1 = random.choice(odpovedi_17)
        time.sleep(random.randint(0, 2))
        print(ans)
        time.sleep(random.randint(0, 5))
        print(ans1)
    else:
        time.sleep(random.randint(0, 5))
        print(ans)
#
def dreams_11():
    answers=["Sny se mi zdají jen občasně","Sny se mi skoro vůbec nezdají", "Nevim","Nekdy jo někdy ne.", "NameError: name"]
    for x in range(1):
        resp = random.choice(answers)
    print(resp)
#
def food_12():
    answers = ["pizza","svíčková","guláš","burger","palačinky","kebab","chutná mi tatarák"," mám rád lívance","Error_404"]
    for x in range(1):
        ans = random.choice(answers)
    print(ans)
#
def weather_21():
    answers=["Dobrý den, venku vypadá krásně. Takže určitě bude sluníčko. Ptejte se dál! Ráda bych vám pomohla :)",
      "Dobrý den, vidím na nebi jsou černé mraky, zatím nebude pršet, ale až odpoledne určitě bude",
      "BUDE BOUŘKA!",
      "Prosím pokud jdete ven, tak vemte s sebou i deštník nebo pláštěnku. Bude dnes pršet, možná přijde i bouřka"]

    for x in range(1):
        resp=random.choice(answers)
    print(resp)
# 
def vstavani_22():
    answers = ["Každej den v 8.","Error_404","Záleží na tom kdy se probudím","Obvykle v 10.","Až na oběd.","jeste nez vyjde slunce","Pokaždý jinak","někdy v 8 a někdy v9"]
    for x in range(1):
        ans = random.choice(answers)
    print(ans)    

#
def human_1():
    myAnswers = ["Ano, jsem člověk", "Ale jo, snad jo :-)", "Občas si tím nejsem zcela jistý, zvlášť po víkendu", "No doufám, že ano :-)", "Ne, jsem robot"]
    if manOrWoman == True:
        print("Musím být člověk, jsem přeci " + gender)
    else:
        bestAnswer = random.randint(0,4)
        print(myAnswers[bestAnswer])
        
# body
if answer == 1:
    time.sleep(1)
    human_1()
elif answer == 4:
    time.sleep(1)
    lunch_4()
elif answer == 6:
    time.sleep(1)
    matika_6()
elif answer == 21:
    time.sleep(1)
    weather_21()
elif answer == 22:
    time.sleep(1)
    vstavani_22()
elif answer == 20:
    time.sleep(1)
    Kenobi_20()
elif answer == 11:
    time.sleep(1)
    dreams_11()    
elif answer == 17:
    time.sleep(1)
    Siblings_17()
elif answer == 12:
    time.sleep(1)
    food_12()    






# print(answer)
# print(type(answer))