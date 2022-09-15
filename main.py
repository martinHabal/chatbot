import random
import time
#definuju boolean jestli už se ptal na muže nebo ženu
answer = ""
manOrWoman = True
gender = "muž"
passedQuestion = []

print("Vítejte v obdobě Turingova testu")
print("Z 21 ti otázek jste si vybral/a 7 a ty mi můžete pokládat v jakémkoliv pořadí")

firstAnswer = ["S čím vám mohu pomoci? ", "Tak se ptejte ", "Tak poslouchám "]
answers = ["Máte další otázku?", "Co by vás dále zajímalo?", "Můžete se ptát dál", "A dál?", "Ještě něco?"]
lastAnswer = "Máte poslední otázku"

randomFirstAnswer = random.choice(firstAnswer)#random jen na začátku
randomAnswer = random.choice(answers)#volat random pokaždé znovu ve fci


# kdyz se predtim zepta jestli jsem muz nebo zena, tak napisu, kdyj jsem zena, jsem preci take clovek
# osetrit ze se zepta dvakrat na stejnou otazku

#
def lunch_4():
    answers = ["Dneska jsem si dal k obědu kebab","Oběd jsem dneska ještě neměl","Oběd si dám až později"]

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
    
    resp=random.choice(answers)
    print(resp)
#
def name_8(*seznam_jmen):#tohle zkontrolovat
    print("Moje jméno je " + random.choice(seznam_jmen) + ".")

time.sleep(5)  
name_8 ("Honza", "Jakub", "Michal", "Anička", "Jirka", "Filip", "Daniela", "Michael", "Tomáš", "Christian", "Robert", "Alexej", "Daniel")

time.sleep(5)
print("")
print("A jak se jmenuješ ty?")
print("")
jmeno = input()
print("")
time.sleep(10)
x = ["Máš krásné jméno :3", "Fakt pěkné jméno :)", "Promiň, ale tohle je příšerné jméno. Kdo ti ho dal!?"]
print(jmeno + "? " + random.choice(x))
#
def Kenobi_20():
    obi = ['Obivan Kenobi je hlavní postava z filmu StarWars.', 'Obi-Wan Kenobi je fiktivní postava ze Star Wars, jedna z ústředních postav celé ságy.', 'Nevím asi nějaká postava z filmu.']
    rndobi = random.choice(obi)
    print(rndobi)
#
def Siblings_17():
    odpovedi_17 = ["Co to je za blbo0u otázku? Samozřejmě že ano!", "... Dej mi chvilku.", "Ano", "Jo, asi ano.", "Nemám, protože jsem počítač.", "1101110 1100101 1101101 111111 111111", "Mám sourozence. Mám jednoho bratra a jednu sestru."]
    
    
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
    
    resp = random.choice(answers)
    print(resp)
#
def food_12():
    answers = ["pizza","svíčková","guláš","burger","palačinky","kebab","chutná mi tatarák"," mám rád lívance","Error_404"]
    
    ans = random.choice(answers)
    print(ans)
#
def Breeding_13():
    odpovedi_13 = ["To fakt nevim. Netušim.", "Asi se stane něco fakt děsivýho.", "Však to ani biologicky není možný, ne?", "Vzikne vám ježala.", "Asi vznikne tvor, který se musí jen plazit.", "Tak to vím co vzinke. Vznikne nám alfa žížala s kopytama."]
    
    pickOne = random.choice(odpovedi_13)
    if pickOne == odpovedi_13[0]:
        time.sleep(5)
        print(pickOne)
    elif pickOne == odpovedi_13[1]:
        time.sleep(6)
        print(pickOne)
    elif pickOne == odpovedi_13[2]:
        time.sleep(8)
        print(pickOne)
    elif pickOne == odpovedi_13[3]:
        time.sleep(2)
        print(pickOne)
    elif pickOne == odpovedi_13[4]:
        time.sleep(7)
        print(pickOne)
    elif pickOne == odpovedi_13[5]:
        time.sleep(8)
        print(pickOne)    
#
def weather_21():
    answers=["Dobrý den, venku vypadá krásně. Takže určitě bude sluníčko. Ptejte se dál! Ráda bych vám pomohla :)",
      "Dobrý den, vidím na nebi jsou černé mraky, zatím nebude pršet, ale až odpoledne určitě bude",
      "BUDE BOUŘKA!",
      "Prosím pokud jdete ven, tak vemte s sebou i deštník nebo pláštěnku. Bude dnes pršet, možná přijde i bouřka"]

    resp=random.choice(answers)
    print(resp)
# 
def vstavani_22():
    answers = ["Každej den v 8.","Error_404","Záleží na tom kdy se probudím","Obvykle v 10.","Až na oběd.","jeste nez vyjde slunce","Pokaždý jinak","někdy v 8 a někdy v9"]
    
    ans = random.choice(answers)
    print(ans)    

#
def human_1():
    myAnswers = ["Ano, jsem člověk", "Ale jo, snad jo :-)", "Občas si tím nejsem zcela jistý, zvlášť po víkendu", "No doufám, že ano :-)", "Ne, jsem robot"]
    if manOrWoman == True:
        print("Musím být člověk, jsem přeci " + gender)
        time.sleep(2)
        randomAnswer = random.choice(answers)
        answer = int(input(randomAnswer))
        options()
    else:
        bestAnswer = random.randint(0,4)
        print(myAnswers[bestAnswer])
        randomAnswer = random.choice(answers)
        answer = int(input(randomAnswer))
        options()
        
# body
answer = int(input(randomFirstAnswer))

def options():

    if answer == 1:
        time.sleep(1)
        human_1()
    elif answer == 4:
        time.sleep(1)
        lunch_4()
    elif answer == 6:
        time.sleep(1)
        matika_6()
    elif answer == 7:
        time.sleep(1)
        movies_7()    
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
    elif answer == 13:
        time.sleep(1)
        Breeding_13()       
    elif answer == 17:
        time.sleep(1)
        Siblings_17()
    elif answer == 12:
        time.sleep(1)
        food_12()    
    else:
        print("Tak na tuto otázku neznám odpověď")
        time.sleep(1)
        # options()

options()

#musime doresit jak se bude pokladat dalsi otazka na konci fce, asi bude lepsi at si tam kazdej tu otazku dopise sam
#osetrit aby se nemohl zeptat na tu samou otazku, Honza se o to postará
# print(answer)
# print(type(answer))
