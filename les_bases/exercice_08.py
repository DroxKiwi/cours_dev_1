# ============================================
# EXERCICE 8 : Fonctions avec return
# ============================================
#
# OBJECTIF : Créer des fonctions qui renvoient une valeur
#
# RAPPEL :
#   def calculer(a, b):
#       resultat = a + b
#       return resultat  # Renvoie la valeur
#
#   reponse = calculer(5, 3)  # reponse vaut 8
# ============================================

# Exemple (celui-ci marche déjà !) :
def doubler(nombre):
    resultat = nombre * 2
    return resultat

mon_nombre = 7
le_double = doubler(mon_nombre)
print("Le double de", mon_nombre, "est", le_double)

print("---")

# À TOI DE JOUER !

# 1. Complète la fonction qui additionne deux nombres

def additionner(a, b):
    resultat = a _____ b  # Quel signe pour additionner ?
    return _____  # Que doit-on renvoyer ?

somme = additionner(10, 5)
print("10 + 5 =", somme)

print("---")

# 2. Complète la fonction qui calcule le prix avec une réduction

def prix_reduit(prix, reduction):
    nouveau_prix = prix - reduction
    _____ nouveau_prix  # Quel mot pour renvoyer ?

prix_final = prix_reduit(100, 20)
print("100 euros avec 20 euros de réduction =", prix_final, "euros")

print("---")

# 3. Crée une fonction qui calcule l'aire d'un rectangle
# (aire = longueur x largeur)

def aire_rectangle(longueur, largeur):
    aire = _____ * _____  # Complète le calcul
    return _____

# Teste ta fonction :
mon_aire = aire_rectangle(5, 3)
print("L'aire d'un rectangle 5x3 est", mon_aire)

print("---")

# 4. DÉFI : Crée une fonction qui dit si un nombre est pair ou impair
# Un nombre est pair s'il est divisible par 2 (reste = 0)
# En Python : nombre % 2 donne le reste de la division par 2

def est_pair(nombre):
    if nombre % 2 == 0:
        return _____  # Renvoie True ou False ?
    else:
        return _____  # Renvoie True ou False ?

# Teste :
print("4 est pair ?", est_pair(4))
print("7 est pair ?", est_pair(7))
