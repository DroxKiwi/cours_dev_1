# ============================================
# EXERCICE 5 : Demander à l'utilisateur avec input()
# ============================================
#
# OBJECTIF : Créer un programme qui pose des questions
#
# RAPPEL :
#   reponse = input("Ta question ? ")
#   -> Le programme attend que tu écrives quelque chose
#   -> Ta réponse est rangée dans la variable "reponse"
# ============================================

# Exemple (celui-ci marche déjà !) :
couleur = input("Quelle est ta couleur préférée ? ")
print("Oh, tu aimes le", couleur, "! C'est joli !")

# À TOI DE JOUER !

# 1. Demande son prénom à l'utilisateur et dis-lui bonjour
# Complète les _____ :

prenom = input("_____")  # Écris une question pour demander le prénom
print("Bonjour", _____, "!")  # Affiche le prénom

# 2. Demande son animal préféré et fais une phrase
# Complète les _____ :

animal = _____("Quel est ton animal préféré ? ")  # Quelle fonction utiliser ?
print("Moi aussi j'adore les", animal, "!")

# 3. Demande l'âge et calcule l'année de naissance (on est en 2026)
# Attention : input() donne du texte, il faut convertir en nombre avec int()

age_texte = input("Quel âge as-tu ? ")
age = int(age_texte)  # On convertit le texte en nombre
annee_naissance = 2026 - _____  # Quel calcul faire ?

print("Tu es né(e) en", annee_naissance)

# 4. DÉFI : Crée ta propre question !
# Le programme doit :
# - Poser une question
# - Récupérer la réponse
# - Afficher une phrase avec la réponse

# Écris ton code ici :
