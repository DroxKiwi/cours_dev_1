# ============================================
# EXERCICE 6 : Les conditions avec if
# ============================================
#
# OBJECTIF : Faire des choix dans un programme
#
# RAPPEL :
#   if condition:
#       # Ce code s'exécute si la condition est vraie
#   else:
#       # Ce code s'exécute si la condition est fausse
#
#   Comparaisons : == (égal), != (différent), > < >= <=
# ============================================

# Exemple (celui-ci marche déjà !) :
meteo = "soleil"

if meteo == "soleil":
    print("Je vais me promener !")
else:
    print("Je reste à la maison.")

# À TOI DE JOUER !

# 1. Complète le code pour vérifier si quelqu'un peut conduire
# (On peut conduire à partir de 18 ans)

age = 16

if age _____ 18:  # Quel signe de comparaison ? (>=, <=, >, <, ==)
    print("Tu peux conduire !")
else:
    print("Tu es trop jeune pour conduire.")

# 2. Complète le code pour vérifier un mot de passe

mot_de_passe_secret = "python123"
mot_de_passe_essai = "python123"

if mot_de_passe_essai _____ mot_de_passe_secret:  # Quel signe pour "égal à" ?
    print("Mot de passe correct ! Bienvenue !")
_____:  # Quel mot pour "sinon" ?
    print("Mot de passe incorrect !")

# 3. Complète le code pour dire si un nombre est positif ou négatif

nombre = -5

if nombre _____ 0:  # Quel signe pour "plus grand que" ?
    print("Le nombre est positif")
else:
    print("Le nombre est négatif ou nul")

# 4. DÉFI : Crée un programme qui demande l'âge et dit si la personne
# est au collège (entre 11 et 14 ans) ou non
# Utilise : input(), int(), if, else

# Écris ton code ici :
