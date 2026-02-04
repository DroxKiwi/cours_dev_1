# ============================================
# EXERCICE 7 : Les fonctions
# ============================================
#
# OBJECTIF : Créer et utiliser des fonctions
#
# RAPPEL :
#   def nom_de_la_fonction():
#       # Code de la fonction
#
#   nom_de_la_fonction()  # Pour appeler la fonction
# ============================================

# Exemple (celui-ci marche déjà !) :
def dire_coucou():
    print("Coucou !")
    print("Comment ça va ?")

# On appelle la fonction :
dire_coucou()

print("---")  # Ligne de séparation

# À TOI DE JOUER !

# 1. Complète la fonction pour qu'elle affiche "Bonjour le monde !"

def saluer():
    _____("Bonjour le monde !")

# Appelle la fonction :
saluer()

print("---")

# 2. Crée une fonction qui affiche les paroles d'une chanson (2-3 lignes)
# Par exemple : "Joyeux anniversaire..."

def chanter():
    print("_____")  # Première ligne
    print("_____")  # Deuxième ligne

# Appelle la fonction :
_____()  # Quel est le nom de la fonction ?

print("---")

# 3. Complète la fonction qui prend un prénom en paramètre

def dire_bonjour(prenom):
    print("Bonjour", _____, "!")  # Utilise le paramètre

# Appelle la fonction avec différents prénoms :
dire_bonjour("Marie")
dire_bonjour("Lucas")
dire_bonjour("_____")  # Mets ton prénom !

print("---")

# 4. Crée une fonction qui prend un nombre et affiche sa table de multiplication
# (juste les 3 premiers : nombre x 1, nombre x 2, nombre x 3)

def table_multiplication(nombre):
    print(nombre, "x 1 =", nombre * 1)
    print(nombre, "x 2 =", nombre * _____)
    print(nombre, "x 3 =", _____ * 3)

# Teste avec le nombre 5 :
table_multiplication(5)
