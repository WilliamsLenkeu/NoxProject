def accueil():

    salut()
    print('''
                                  .........       
                                .           .    
                               .             .
                              .   ▢       ▢   .    
                             .                 .   
                             .        ¤        .
                              .               .
                               .    _____    . 
                                .           .
                                  .........
    ''')

    print("1. Determiner si une année est bissextile")
    print("2. Calculer l'Indice de Masse Corporel(IMC) ")
    print("3. Calculer le pourcentage d'amour")
    print("4. Voire des tables de multiplications")
    print("5. Jouer à une chasse au trésor")
    print("6. Jouer au Shifumi")
    print("7. Additionner des valeurs")
    print("8. Determiner la somme des dépenses en boisson")
    print("9. Jouer au casino")
    print("10. Faire un cryptage")
    print("11. Jouer au blackjack")
    print("12. Jouer à deviner le bon nombre")
    print("13. Se déconnecter")
    print("14. Quitter le programme")
    choix()


def choix():

    selection = input("Que voulez vous que je fasse ?  ")
    if selection == "1":
        bissextile()
    elif selection == "2":
        imc()
    elif selection == "3":
        love_percent()
    elif selection == "4":
        multiplication()
    elif selection == "5":
        game()
    elif selection == "6":
        shifumi()
    elif selection == "7":
        additioneuse()
    elif selection == "8":
        calcul_boisson()
    elif selection == "9":
        casino()
    elif selection == "10":
        crypt()
    elif selection == "11":
        blackjack()
    elif selection == "12":
        guessing()
    elif selection == "13":
        deconnect()
    elif selection == "14":
        out()
    else:
        retour()

def deconnect():

    proposition()


def proposition():
    print("1. S'enregistrer comme utlisateur")
    print("2. Se connecter à son compte utilsateur")
    print("3. Quitter le programme")
    select = input()
    if select == "1":
        user = input("Entrer un nom d'utilisateur:  ")
        pwd = input("Entrer votre mot de passe:  ")
        enregistrer_user(user, pwd)
        accueil()
    elif select == "2":
        connexion()
    elif select == "3":
        out()
    else:
        print("Veuillez entrer une valeur correcte")
        proposition()

def connexion():

    user = input("Entrer votre nom d'utilisateur:  ")
    pwd = input("Entrer votre mot de passe:  ")
    us = recup_user()
    pw = recup_pwd()
    if us != user:
        print("Vous n'êtes pas enregistrer comme utilisateur")
        sel = input("Voulez vous vous enregistrer ? (O/N) ").lower()
        if sel == "o":
            user = input("Entrer un nom d'utilisateur:  ")
            pwd = input("Entrer votre mot de passe:  ")
            enregistrer_user(user, pwd)
        elif sel == "n":
            proposition()
        else:
            print("Veuillez entrer une valeur correcte")
            print("Vous serez renvoyé à la page d'accueil")
            proposition()
    elif pw != pwd:
        print("Votre mot de passe est invalide")
        print("vous serez renvoyé vers la page d'accueil")
        proposition()
    else:
        accueil()

nom_fichier_user = "user"
nom_fichier_pwd = "password"

def recup_user():
    import pickle
    import os

    if os.path.exists(nom_fichier_user):
        fichier_user = open(nom_fichier_user, "rb")
        mon_depickler = pickle.Unpickler(fichier_user)
        user = mon_depickler.load()
        fichier_user.close()
    else:
        user = {}
    return user

def salut():

    user = recup_user()
    print("Bienvenue ", user)

def enregistrer_user(user, pwd):
    import pickle
    fichier_user = open(nom_fichier_user, "wb")
    mon_pickler = pickle.Pickler(fichier_user)
    mon_pickler.dump(user)
    fichier_user.close()
    fichier_pwd = open(nom_fichier_pwd, "wb")
    mon_pickler = pickle.Pickler(fichier_pwd)
    mon_pickler.dump(pwd)
    fichier_pwd.close()

def recup_pwd():
    import pickle
    import os
    if os.path.exists(nom_fichier_pwd):
        fichier_pwd = open(nom_fichier_pwd, "rb")
        mon_depickler = pickle.Unpickler(fichier_pwd)
        pwd = mon_depickler.load()
        fichier_pwd.close()
    else:
        pwd = {}
    return pwd


def enregistrer_pwd(pwd):
    import pickle
    fichier_pwd = open(nom_fichier_pwd, "wb")
    mon_pickler = pickle.Pickler(fichier_pwd)
    mon_pickler.dump(pwd)
    fichier_pwd.close()


def retour():

    print("Vous n'avez pas entrer une valeur correcte")
    choix()


def out():
    quit()


def bissextile(os=None):

    print("Bienvenue !!")
    an = input("Entrer une année : ")
    try:
        an = int(an)
        assert an > 0
    except AssertionError:
        print("Veuillez entrer une année supérieure à 0")
    except ValueError:
        print("Veuillez entrer une année valide")
    else:
        if (an % 4) == 0 and (an != 100) == 0 and (an % 400) == 0:
            print("Cette année est bissextile")
        else:
            print("Cette année n'est pas bissextile")

    quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
    if quitter == "o" or quitter == "O":
        print("Vous avez été redirigée vers la page d'accueil .^_____^)")
        accueil()
    elif quitter == "n" or quitter == "N":
        bissextile()
    else:
        print("Entrer une valeur correcte")
        quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
        if quitter == "o" or quitter == "O":
            print(" Vous avez été redirigée vers la page d'accueil .")
            os.system("cls")
            accueil()
        elif quitter == "n" or quitter == "N":
            bissextile()
        else:
            print("Entrer une valeur correcte")


def imc():

    height = input("Entrer votre taille en mètres: ")
    weight = input("Entrer votre poids en Kilogramme: ")

    weight_as_int = int(weight)
    height_as_float = float(height)

    bmi = weight_as_int / (height_as_float * height_as_float)

    bmi_as_int = int(bmi)

    print("Votre IMC est :", bmi_as_int)
    quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
    if quitter == "o" or quitter == "O":
        print("Vous avez été redirigée vers la page d'accueil .^_____^)")
        accueil()
    elif quitter == "n" or quitter == "N":
        imc()
    else:
        print("Entrer une valeur correcte")
        quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
        if quitter == "o" or quitter == "O":
            print("Vous avez été redirigée vers la page d'accueil .^_____^)")
            accueil()
        elif quitter == "n" or quitter == "N":
            imc()
        else:
            print("Entrer une valeur correcte")


def love_percent():

    print("Bienvenue dans le calculateur d'amour!")
    name1 = input("Quel est votre nom ? \n")
    name2 = input("Quel est son nom ? \n")

    name1 = name1.lower()
    name2 = name2.lower()
    r1 = name1.count("t") + name2.count("t")
    r2 = name1.count("r") + name2.count("r")
    r3 = name1.count("u") + name2.count("u")
    r4 = name1.count("e") + name2.count("e")
    r5 = name1.count("l") + name2.count("l")
    r6 = name1.count("o") + name2.count("o")
    r7 = name1.count("v") + name2.count("v")
    r8 = name1.count("e") + name2.count("e")
    re1 = r1 + r2 + r3 + r4
    re2 = r5 + r6 + r7 + r8
    re1 = str(re1)
    re2 = str(re2)
    re3 = re1 + re2
    re3 = int(re3)
    if re3 <= 10 or re3 >= 90:
        print("Your score is", re3, ", you go together like coke and mentos.")
    elif (re3 >= 40) and (re3 <= 50):
        print("Your score is", re3, ", you are alright together.")
    else:
        print("Your score is", re3, ".")

    quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
    if quitter == "o" or quitter == "O":
        print("Vous avez été redirigée vers la page d'accueil .^_____^)")
        accueil()
    elif quitter == "n" or quitter == "N":
        love_percent()
    else:
        print("Entrer une valeur correcte")
        quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
        if quitter == "o" or quitter == "O":
            print("Vous avez été redirigée vers la page d'accueil .^_____^)")
            accueil()
        elif quitter == "n" or quitter == "N":
            love_percent()
        else:
            print("Entrer une valeur correcte")


def multiplication():

    val = input("Entrer le chiffre dont vous voulez la table de multiplication : ")

    val = int(val)
    i = 0
    while i < 10:
        mul = i + 1
        print(mul, " * ", val, " = ", mul * val)
        i += 1

    quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
    if quitter == "o" or quitter == "O":
        print("Vous avez été redirigée vers la page d'accueil .^_____^)")
        accueil()
    elif quitter == "n" or quitter == "N":
        multiplication()
    else:
        print("Entrer une valeur correcte")
        quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
        if quitter == "o" or quitter == "O":
            print("Vous avez été redirigée vers la page d'accueil .^_____^)")
            accueil()
        elif quitter == "n" or quitter == "N":
            multiplication()
        else:
            print("Entrer une valeur correcte")


def game():

    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Bienvenue sur l'île au trésor.")
    print("Votre mission est de trouver le trésor.")

    choice1 = input('Vous êtes entrain de traverser une route. Où voulez vous aller? "gauche" ou "droite" \n').lower()
    if choice1 == "gauche":
        choice2 = input('Vous êtes arrivés au lac. Il y a une île au milieu du lac. "attendre" pour attendre un bateau ou "nager" pour y aller à la nage. \n').lower()
        if choice2 == "attendre":
            choice3 = input("Vous êtes arrivés à l'île sans arme. Il y a une maison avec trois portes. Une rouge, Une jaune et une bleu. Quelle couleur choissisez vous? \n").lower()
            if choice3 == "rouge":
                print("Cette salle est en feu et vous mourrez. Game Over.")
            elif choice3 == "jaune":
                print("Vous avez trouvé le trésor! You Win!")
            elif choice3 == "blue":
                print("Vous êtes entré dans un nid de bêtes. Game Over.")
            else:
                print("Vous avez pris une porte qui n'existe pas. Game Over.")
        else:
            print("Vous avez été mangé par des piranhas. Game Over.")
    else:
        print("Vous êtes tombé dans un trou . Game Over.")

    quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
    if quitter == "o" or quitter == "O":
        print("Vous avez été redirigée vers la page d'accueil .^_____^)")
        accueil()
    elif quitter == "n" or quitter == "N":
        game()
    else:
        print("Entrer une valeur correcte")
        quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
        if quitter == "o" or quitter == "O":
            print("Vous avez été redirigée vers la page d'accueil .^_____^)")
            accueil()
        elif quitter == "n" or quitter == "N":
            game()
        else:
            print("Entrer une valeur correcte")


def shifumi():
    import random

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    image_rep = [rock, paper, scissors]

    choix_joueur = int(input("Que choisis tu ? Tape 0 pour la Pierre, 1 pour le papier et 2 pour le ciseau.\n"))
    print(image_rep[choix_joueur])

    choix_machine = random.randint(0, 2)
    print("Choix de l'ordinateur:")
    print(image_rep[choix_machine])

    if choix_joueur >= 3 or choix_joueur < 0:
        print("vous avez tapé un numéro invalide, vous avez perdu!")
    elif choix_joueur == 0 and choix_machine == 2:
        print("!!!Victoire!!!")
    elif choix_machine == 0 and choix_joueur == 2:
        print("!!!Perdu!!!")
    elif choix_machine > choix_joueur:
        print("!!!Perdu!!!")
    elif choix_joueur > choix_machine:
        print("!!!Victoire!!!")
    elif choix_machine == choix_joueur:
        print("C'est un match nul")

    quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
    if quitter == "o" or quitter == "O":
        print("Vous avez été redirigée vers la page d'accueil .^_____^)")
        accueil()
    elif quitter == "n" or quitter == "N":
        shifumi()
    else:
        print("Entrer une valeur correcte")
        quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
        if quitter == "o" or quitter == "O":
            print("Vous avez été redirigée vers la page d'accueil .^_____^)")
            accueil()
        elif quitter == "n" or quitter == "N":
            shifumi()
        else:
            print("Entrer une valeur correcte")


def calcul_boisson():

    print("Bienvenue dans le générateur de Paiement!")
    bill = input("Quelle est le montant totale de la facture? ")
    tip = input("Quelle taux de pourboire voulez vous donnez? 10, 12, or 15? ")
    people = input("Combien de personne payent la facture? ")
    bill = float(bill)
    bonus = bill * (int(tip) / 100)
    bill2 = bill + bonus
    final_bill = bill2 / int(people)
    final_bill = round(final_bill, 2)
    final_bill = "{:.2f}".format(final_bill)
    print(final_bill)

    quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
    if quitter == "o" or quitter == "O":
        print("Vous avez été redirigée vers la page d'accueil .^_____^)")
        accueil()
    elif quitter == "n" or quitter == "N":
        calcul_boisson()
    else:
        print("Entrer une valeur correcte")
        quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
        if quitter == "o" or quitter == "O":
            print("Vous avez été redirigée vers la page d'accueil .^_____^)")
            accueil()
        elif quitter == "n" or quitter == "N":
            calcul_boisson()
        else:
            print("Entrer une valeur correcte")


def additioneuse():

    two_digit_number = input("Type a two digit number: ")
    a = two_digit_number[0]
    b = two_digit_number[1]
    a = int(a)
    b = int(b)
    print(a + b)

    quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
    if quitter == "o" or quitter == "O":
        print("Vous avez été redirigée vers la page d'accueil .^_____^)")
        accueil()
    elif quitter == "n" or quitter == "N":
        additioneuse()
    else:
        print("Entrer une valeur correcte")
        quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
        if quitter == "o" or quitter == "O":
            print("Vous avez été redirigée vers la page d'accueil .^_____^)")
            accueil()
        elif quitter == "n" or quitter == "N":
            additioneuse()
        else:
            print("Entrer une valeur correcte")


def crypt():

    val = input("Entrer une valeur : ")
    for lettre in val:
        if lettre in "azertyuioqsdhklwxcvbn" or ",;:!?./§%µù*¨£^$~#{[|`\^@]}/*-+":
            print(lettre)
        else:
            print("*")

    quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
    if quitter == "o" or quitter == "O":
        print("Vous avez été redirigée vers la page d'accueil .^_____^)")
        accueil()
    elif quitter == "n" or quitter == "N":
        crypt()
    else:
        print("Entrer une valeur correcte")
        quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
        if quitter == "o" or quitter == "O":
            print("Vous avez été redirigée vers la page d'accueil .^_____^)")
            accueil()
        elif quitter == "n" or quitter == "N":
            crypt()
        else:
            print("Entrer une valeur correcte")


def casino():

    argent = 1000
    continuer_partie = True
    from random import randrange
    from math import ceil

    print(" Vous vous installez à la table de roulette avec ", argent, "$.")

    while continuer_partie:

        nombre_mise = -1
        while nombre_mise < 0 or nombre_mise > 49:
            nombre_mise = input(" Tapez le nombre sur lequel vous voulez miser ( entre 0 et 49) : ")

            try:
                nombre_mise = int(nombre_mise)
            except ValueError:
                print(" Vous n'avez pas saisi de nombre ")
                nombre_mise = -1
                continue
            if nombre_mise < 0:
                print("Ce nombre est négatif ")
            if nombre_mise > 49:
                print("Ce nombre est supérieur à 49")

        mise = 0
        while mise <= 0 or mise > argent:
            mise = input(" Tapez le montant de votre mise : ")

            try:
                mise = int(mise)
            except ValueError:
                print(" Vous n'avez pas saisi de nombre ")
                mise = -1
                continue
            if mise <= 0:
                print("La mise saisie est négative ou nulle .")
            if mise > argent:
                print(" Vous ne pouvez miser autant , vous n'avez que", argent, "$")

        numero_gagnant = randrange(50)
        print("La roulette tourne ... ... et s'arrête sur le numéro", numero_gagnant)

        if numero_gagnant == nombre_mise:
            print("Félicitations ! Vous obtenez ", mise * 3, "$ !")
            argent += mise * 3
        elif numero_gagnant % 2 == nombre_mise % 2:
            mise = ceil(mise * 0.5)
            print(" Vous avez misé sur la bonne couleur . Vous obtenez ", mise, "$")
            argent += mise
        else:
            print("Désolé l'ami , c'est pas pour cette fois . Vous perdez votre mise .")
            argent -= mise

        if argent <= 0:
            print(" Vous ê tes ruin é ! C'est la fin de la partie .")
            continuer_partie = False
        else:

            print(" Vous avez à pré sent ", argent, "$")
            quitter = input(" Souhaitez - vous quitter le casino (o/n)? ")
            if quitter == "o" or quitter == "O":
                print(" Vous quittez le casino avec vos gains .")
                continuer_partie = False
                accueil()

def blackjack():
    import random

    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
    def deal_card():
        """Returns a random card from the deck."""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards"""

        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_scor, computer_scor):
        if user_scor > 21 and computer_scor > 21:
            return "You went over. You lose 😤"

        if user_scor == computer_scor:
            return "Draw 🙃"
        elif computer_scor == 0:
            return "Perdu, votre opposant à fait un blackjack 😱"
        elif user_scor == 0:
            return "Gagné vous avez fait un blackjack 😎"
        elif user_scor > 21:
            return "You went over. You lose 😭"
        elif computer_scor > 21:
            return "Opponent went over. You win 😁"
        elif user_scor > computer_scor:
            return "You win 😃"
        else:
            return "You lose 😤"

        quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
        if quitter == "o" or quitter == "O":
            print("Vous avez été redirigée vers la page d'accueil .^_____^)")
            accueil()
        elif quitter == "n" or quitter == "N":
            bissextile()
        else:
            print("Entrer une valeur correcte")
            quitter = input(" Souhaitez - vous rentrer à la page d'accueil (o/n)? ")
            if quitter == "o" or quitter == "O":
                print(" Vous avez été redirigée vers la page d'accueil .")
                os.system("cls")
                accueil()
            elif quitter == "n" or quitter == "N":
                bissextile()
            else:
                print("Entrer une valeur correcte")

    def play_game():

        global computer_score, user_score
        print(logo)

        user_cards = []
        computer_cards = []
        is_game_over = False

        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"   Vos cartes: {user_cards}, votre score actuel: {user_score}")
            print(f"   première carte de l'ordinateur: {computer_cards[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                user_should_deal = input("Entrer 'y' pour recevoir une autre carte, Entrer 'n' pour passer le tour: ")
                if user_should_deal == "y":
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"   Votre main final: {user_cards}, votre score final: {user_score}")
        print(f"   La main finale de l'ordinateur: {computer_cards}, votre score final: {computer_score}")
        print(compare(user_score, computer_score))

    sel = input("Vous voulez jouer au jeu du blackjack? Type 'y' or 'n': ")
    if sel == "y":
         play_game()
    elif sel == "n":
         accueil()
    else:
        print("Entrer une valeur correcte")
        blackjack()

def guessing():
    from random import randint

    logo = """
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """

    EASY_LEVEL_TURNS = 10
    HARD_LEVEL_TURNS = 5

    def check_answer(guess, answer, turns):
        if guess > answer:
            print("C'est grand.")
            return turns - 1
        elif guess < answer:
            print("C'est petit.")
            return turns - 1
        else:
            print(f"Tu as trouvé! La réponse est {answer}.")
            sel = input("Voulez vous rentrer à la page d'accueil ? (O/N)   ").lower()
            if sel == "o":
                accueil()
            elif sel == "n":
                rep()
            else:
                print("Entrer une valeur correcte")
                rep()

    def set_difficulty():
        level = input("Choissisez le niveau de difficultés. Type 'easy' or 'hard': ")
        if level == "easy":
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS

    def rep():
        sel = input("Voulez vous jouer à deviner le bon chiffre ?(O/N)  ").lower()
        if sel == "o":
            jeu()
        elif sel == "n":
            accueil()
        else:
            print("Entrer une valeur correcte")
            rep()

    def jeu():
        print(logo)
        print("Bienvenue dans le devinateur de nombre!")
        print("Je pense à un nombre entre 1 et 100.")
        answer = randint(1, 100)
        #print(f"Pssst, la bonne réponse est {answer}")

        turns = set_difficulty()
        guess = 0
        while guess != answer:
            print(f"Tu as {turns} pour trouver la réponse.")

            guess = int(input("Make a guess: "))

            turns = check_answer(guess, answer, turns)
            if turns == 0:
                print("Tu n'as pas deviné, Tu as perdu.")
                print(f"Pssst, la bonne réponse est {answer}")
                return
            elif guess != answer:
                print("Devine encore.")
    rep()
