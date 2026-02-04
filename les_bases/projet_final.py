# ============================================
# PROJET FINAL : Le jeu de devinette !
# ============================================
#
# Tu vas créer un jeu où l'ordinateur choisit un nombre secret
# et le joueur doit le deviner !
#
# Ce projet utilise TOUT ce que tu as appris :
# - Les variables
# - print() et input()
# - Les conditions if/else
# - Les fonctions
# ============================================

# Le nombre secret (tu peux le changer pour tester)
nombre_secret = 7

# 1. Complète la fonction qui vérifie la réponse du joueur

def verifier_reponse(essai, secret):
    """
    Cette fonction compare l'essai du joueur avec le nombre secret.
    Elle renvoie True si c'est correct, False sinon.
    """
    if essai == secret:
        return _____  # Correct ! Renvoie True ou False ?
    else:
        return _____  # Incorrect ! Renvoie True ou False ?

# 2. Complète la fonction qui donne un indice

def donner_indice(essai, secret):
    """
    Cette fonction dit si le nombre est trop grand ou trop petit.
    """
    if essai > secret:
        print("C'est trop grand ! Essaie plus petit.")
    _____:  # Quel mot pour "sinon" ?
        print("C'est trop petit ! Essaie plus grand.")

# 3. Le programme principal - Complète les _____ !

print("=" * 40)
print("   BIENVENUE DANS LE JEU DE DEVINETTE !")
print("=" * 40)
print()
print("Je pense à un nombre entre 1 et 10.")
print("Essaie de le deviner !")
print()

# Demande un nombre au joueur
reponse_texte = input("Entre ton nombre : ")
reponse = int(reponse_texte)  # Convertit en nombre

# Vérifie la réponse
resultat = verifier_reponse(reponse, nombre_secret)

if resultat == True:
    print()
    print("🎉 BRAVO ! Tu as trouvé ! Le nombre était bien", _____)  # Affiche le nombre secret
    print("Tu es trop fort(e) !")
else:
    print()
    donner_indice(_____, _____)  # Quels paramètres donner ? (l'essai et le secret)
    print("Le nombre secret était", nombre_secret)
    print("Rejoue pour gagner !")

print()
print("Merci d'avoir joué ! À bientôt !")

# ============================================
# BONUS : Améliore le jeu !
# ============================================
# Idées pour aller plus loin :
# - Donne plusieurs essais au joueur (avec une boucle while)
# - Fais choisir le nombre secret au hasard (avec random)
# - Ajoute un compteur d'essais
# ============================================
