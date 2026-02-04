# 🐍 Apprendre Python - Mon Premier Cours de Programmation

Bienvenue dans ce cours de programmation ! Tu vas apprendre à coder en Python, un langage utilisé par des millions de développeurs dans le monde.

---

## 📚 Comment utiliser ce cours ?

1. Lis chaque chapitre attentivement
2. Ouvre le fichier d'exercice correspondant
3. Complète l'exercice en suivant les instructions
4. Lance le programme pour voir si ça marche !

---

## 🖥️ Guide : Utiliser VS Code (pour les débutants)

### Étape 1 : Ouvrir le dossier du cours dans VS Code

1. **Lance VS Code** en double-cliquant sur son icône sur le bureau (ou cherche "Visual Studio Code" dans le menu Démarrer)
2. **Ouvre le dossier du cours :**
   - Clique sur **Fichier** (en haut à gauche) → **Ouvrir le dossier...**
   - Navigue jusqu'au dossier `les_bases` (là où se trouvent les fichiers d'exercices)
   - Clique sur **Sélectionner un dossier**
3. Tu devrais maintenant voir la liste des fichiers sur le côté gauche de l'écran (c'est l'**Explorateur de fichiers**)

### Étape 2 : Ouvrir un fichier d'exercice

1. **Regarde le panneau de gauche** : tu vois la liste des fichiers (`exercice_01.py`, `exercice_02.py`, etc.)
2. **Clique une fois** sur le fichier que tu veux ouvrir (par exemple `exercice_01.py`)
3. Le contenu du fichier s'affiche dans la zone principale de VS Code
4. Tu peux maintenant **modifier le code** en cliquant dans cette zone et en tapant au clavier

### Étape 3 : Sauvegarder ton travail

**TRÈS IMPORTANT !** Après avoir modifié un fichier, il faut le sauvegarder :
- Appuie sur **Ctrl + S** (garde le doigt sur Ctrl, puis appuie sur S)
- OU clique sur **Fichier** → **Enregistrer**

💡 **Astuce :** Si tu vois un **point blanc** à côté du nom du fichier en haut, ça veut dire que tu as des modifications non sauvegardées !

### Étape 4 : Ouvrir le terminal dans VS Code

Le **terminal**, c'est l'endroit où tu vas taper des commandes pour lancer tes programmes Python.

1. **Ouvre le terminal :** 
   - Clique sur **Terminal** (dans la barre de menu en haut) → **Nouveau terminal**
   - OU utilise le raccourci clavier : **Ctrl + ù** (ou **Ctrl + `** selon ton clavier)
2. **Un panneau apparaît en bas de l'écran** : c'est le terminal !
3. Tu devrais voir quelque chose comme `PS C:\...\les_bases>` suivi d'un curseur clignotant

### Étape 5 : Lancer un programme Python

Maintenant que le terminal est ouvert, tu peux lancer ton programme :

1. **Tape la commande suivante** dans le terminal :
   ```
   python exercice_01.py
   ```
   (remplace `exercice_01.py` par le nom du fichier que tu veux lancer)

2. **Appuie sur la touche Entrée** (la grande touche à droite du clavier)

3. **Regarde le résultat** qui s'affiche dans le terminal !

### ❌ Si tu as une erreur

- **"python n'est pas reconnu"** → Python n'est pas installé correctement. Demande de l'aide à ton professeur.
- **"No such file or directory"** → Vérifie que tu es dans le bon dossier et que le nom du fichier est correct.
- **Erreur dans le code** → Lis le message d'erreur, il t'indique souvent la ligne du problème. Corrige ton code et réessaye !

### 🔄 Résumé : La routine pour chaque exercice

1. 📖 Lis le chapitre dans ce fichier README
2. 📂 Clique sur le fichier d'exercice correspondant (à gauche)
3. ✏️ Modifie le code pour compléter l'exercice
4. 💾 Sauvegarde avec **Ctrl + S**
5. 💻 Ouvre le terminal (**Terminal** → **Nouveau terminal**)
6. ▶️ Tape `python nom_du_fichier.py` et appuie sur **Entrée**
7. 👀 Regarde si ça fonctionne !

---

## Chapitre 1 : C'est quoi un programme ?

Un **programme**, c'est comme une recette de cuisine. C'est une liste d'instructions que l'ordinateur va suivre, une par une, dans l'ordre.

Par exemple, pour faire un gâteau :
1. Prendre les œufs
2. Casser les œufs
3. Ajouter la farine
4. Mélanger

En programmation, c'est pareil ! On écrit des instructions et l'ordinateur les exécute.

---

## Chapitre 2 : Afficher du texte avec `print()`

La première chose qu'on apprend, c'est comment faire parler l'ordinateur !

Pour afficher du texte à l'écran, on utilise la commande `print()` :

```python
print("Bonjour tout le monde !")
```

### 🔍 Décortiquons cette ligne de code

| Élément | C'est quoi ? | Comment le taper ? |
|---------|--------------|-------------------|
| `print` | Le nom de la commande | Tape les lettres p-r-i-n-t (en minuscules !) |
| `(` | Parenthèse ouvrante | **Maj + 5** sur ton clavier |
| `"` | Guillemet | **Maj + 3** sur ton clavier |
| `Bonjour...` | Le texte à afficher | Tape ce que tu veux afficher |
| `"` | Guillemet fermant | **Maj + 3** à nouveau |
| `)` | Parenthèse fermante | **Maj + °** (la touche à côté du 0) |

### ⚠️ Les erreurs fréquentes des débutants

| Erreur | Problème | Solution |
|--------|----------|----------|
| `Print("Bonjour")` | Le P est en majuscule | Python fait la différence entre majuscules et minuscules. Écris `print` en minuscules |
| `print "Bonjour"` | Il manque les parenthèses | N'oublie pas les `()` autour du texte |
| `print(Bonjour)` | Il manque les guillemets | Le texte doit être entre `"guillemets"` |
| `print("Bonjour)` | Il manque un guillemet | Vérifie que tu as un `"` au début ET à la fin du texte |

### 💡 Astuce : Afficher plusieurs lignes

Tu peux écrire plusieurs `print()` pour afficher plusieurs lignes :

```python
print("Ligne 1")
print("Ligne 2")
print("Ligne 3")
```

Chaque `print()` affiche son texte puis passe à la ligne suivante.

### ✏️ Exercice 1 : Fichier `exercice_01.py`

**Comment faire cet exercice :**

1. **Clique sur `exercice_01.py`** dans le panneau de gauche de VS Code
2. **Lis les instructions** qui sont écrites dans le fichier (les lignes qui commencent par `#` sont des commentaires, elles t'expliquent quoi faire)
3. **Écris ton code** : tape `print("Salut, je m'appelle [ton prénom] !")` en remplaçant `[ton prénom]` par ton vrai prénom
4. **Sauvegarde** avec **Ctrl + S**
5. **Ouvre le terminal** (Terminal → Nouveau terminal)
6. **Lance le programme** en tapant `python exercice_01.py` puis **Entrée**
7. **Vérifie** que ton prénom s'affiche bien dans le terminal !

---

## Chapitre 3 : Les variables - Des boîtes pour ranger des informations

Une **variable**, c'est comme une boîte avec une étiquette. Tu peux y ranger quelque chose et la retrouver plus tard grâce à son nom.

```python
prenom = "Lucas"
age = 13
```

### 🔍 Décortiquons cette ligne de code

Prenons `prenom = "Lucas"` :

| Élément | C'est quoi ? | Explication |
|---------|--------------|-------------|
| `prenom` | Le nom de la variable | C'est l'étiquette de ta boîte. Tu choisis le nom que tu veux ! |
| `=` | Le signe égal | Ça veut dire "ranger dans". Ce n'est PAS une comparaison mathématique ! |
| `"Lucas"` | La valeur | C'est ce qu'on met dans la boîte |

Ici, on a créé :
- Une boîte appelée `prenom` qui contient `"Lucas"`
- Une boîte appelée `age` qui contient `13`

### 📏 Les règles pour nommer une variable

Tu ne peux pas appeler ta variable n'importe comment ! Voici les règles :

| Règle | ✅ Correct | ❌ Incorrect |
|-------|-----------|-------------|
| Pas d'espaces | `mon_age` | `mon age` |
| Pas de chiffre au début | `age1` | `1age` |
| Pas de caractères spéciaux | `prenom` | `prénom` (pas d'accent !) |
| Pas de mots réservés Python | `mon_print` | `print` (c'est déjà utilisé par Python) |

💡 **Conseil :** Utilise des noms qui décrivent ce que contient la variable :
- ✅ `age_utilisateur` → on comprend ce que c'est
- ❌ `x` → on ne sait pas ce que c'est

### 📦 Comment utiliser une variable

```python
prenom = "Lucas"
print(prenom)  # Affiche : Lucas
```

**Attention !** Quand on utilise une variable, on n'utilise PAS de guillemets :
- `print(prenom)` → affiche le contenu de la boîte (Lucas)
- `print("prenom")` → affiche le mot "prenom"

### 🔄 Modifier une variable

Tu peux changer le contenu d'une variable à tout moment :

```python
score = 0
print(score)  # Affiche : 0

score = 10
print(score)  # Affiche : 10

score = 25
print(score)  # Affiche : 25
```

La nouvelle valeur remplace l'ancienne.

### ✏️ Exercice 2 : Fichier `exercice_02.py`

**Comment faire cet exercice :**

1. **Clique sur `exercice_02.py`** dans le panneau de gauche
2. **Lis les commentaires** (lignes commençant par `#`) pour comprendre ce qu'on te demande
3. **Crée tes variables** en tapant par exemple :
   ```python
   prenom = "TonPrenom"
   age = 14
   ```
4. **Affiche-les** avec `print()` :
   ```python
   print(prenom)
   print(age)
   ```
5. **Sauvegarde** (Ctrl + S), **ouvre le terminal**, et **lance** avec `python exercice_02.py`

---

## Chapitre 4 : Les types de variables

Les variables peuvent contenir différents types d'informations. C'est important de connaître les types car Python ne les traite pas de la même façon !

### 📋 Les 4 types principaux

| Type | Nom en Python | Exemple | C'est quoi ? | Comment le reconnaître ? |
|------|---------------|---------|--------------|-------------------------|
| Texte | `str` (string) | `"Bonjour"` | Des mots, des phrases | Il y a des **guillemets** `"..."` |
| Nombre entier | `int` (integer) | `42` | Un nombre sans virgule | C'est un **nombre sans point** |
| Nombre décimal | `float` | `3.14` | Un nombre avec virgule | C'est un nombre **avec un point** |
| Vrai/Faux | `bool` (boolean) | `True` / `False` | Une réponse oui ou non | C'est écrit **True** ou **False** (avec majuscule !) |

### 🔍 Exemples détaillés

```python
nom = "Marie"           # str (texte) → il y a des guillemets
age = 14                # int (nombre entier) → nombre sans point
taille = 1.65           # float (nombre décimal) → nombre avec un point
aime_python = True      # bool (vrai ou faux) → c'est True ou False
```

### ⚠️ Attention aux pièges !

| Valeur | Type | Explication |
|--------|------|-------------|
| `"42"` | str (texte) | Les guillemets en font un TEXTE, pas un nombre ! |
| `42` | int (nombre) | Pas de guillemets = c'est un vrai nombre |
| `"3.14"` | str (texte) | Guillemets = texte |
| `3.14` | float (décimal) | Pas de guillemets + point = nombre décimal |
| `"True"` | str (texte) | Avec guillemets, c'est du texte ! |
| `True` | bool | Sans guillemets et avec majuscule = booléen |

### 💡 Pourquoi c'est important ?

Tu ne peux pas faire de calculs avec du texte !

```python
# ✅ Ça marche :
nombre1 = 5
nombre2 = 3
resultat = nombre1 + nombre2  # resultat = 8

# ❌ Ça ne fait pas ce qu'on veut :
texte1 = "5"
texte2 = "3"
resultat = texte1 + texte2  # resultat = "53" (ça colle les textes !)
```

### 🔧 Comment vérifier le type d'une variable ?

Tu peux utiliser la fonction `type()` :

```python
age = 14
print(type(age))  # Affiche : <class 'int'>

nom = "Lucas"
print(type(nom))  # Affiche : <class 'str'>
```

### ✏️ Exercice 3 : Fichier `exercice_03.py`

**Comment faire cet exercice :**

1. **Ouvre `exercice_03.py`** dans VS Code
2. **Regarde chaque variable** et demande-toi :
   - Y a-t-il des guillemets ? → C'est un `str`
   - C'est un nombre sans point ? → C'est un `int`
   - C'est un nombre avec point ? → C'est un `float`
   - C'est True ou False ? → C'est un `bool`
3. **Écris tes réponses** dans le fichier
4. **Lance le programme** pour vérifier tes réponses

---

## Chapitre 5 : Faire des calculs

Python sait faire des calculs comme une calculatrice !

### 🔢 Les opérations de base

| Opération | Symbole | Comment le taper ? | Exemple | Résultat |
|-----------|---------|-------------------|---------|----------|
| Addition | `+` | **Maj + =** (à côté de la touche Retour arrière) | `5 + 3` | `8` |
| Soustraction | `-` | La touche **6** (sans Maj) | `10 - 4` | `6` |
| Multiplication | `*` | **Maj + ù** (sur certains claviers) ou la touche * du pavé numérique | `6 * 7` | `42` |
| Division | `/` | **Maj + :** (deux points) ou la touche / du pavé numérique | `15 / 3` | `5.0` |

💡 **Note :** Le symbole de multiplication est une **étoile** `*` et non pas une croix `×` !

### 🔍 Exemples étape par étape

**Exemple 1 : Calcul simple**
```python
resultat = 5 + 3
print(resultat)  # Affiche : 8
```

Ce qui se passe :
1. Python calcule `5 + 3` → ça fait `8`
2. Le résultat `8` est rangé dans la variable `resultat`
3. `print()` affiche le contenu de `resultat`

**Exemple 2 : Calcul avec des variables**
```python
pommes = 5
oranges = 3
total = pommes + oranges
print(total)  # Affiche : 8
```

Ce qui se passe :
1. On crée une boîte `pommes` avec `5` dedans
2. On crée une boîte `oranges` avec `3` dedans
3. Python prend le contenu des deux boîtes, les additionne (5 + 3 = 8)
4. Le résultat `8` est rangé dans la variable `total`

### 📝 Plusieurs opérations à la suite

Tu peux combiner plusieurs calculs :

```python
prix_bonbon = 2
quantite = 5
reduction = 3

total = prix_bonbon * quantite - reduction
print(total)  # Affiche : 7
```

Python respecte les priorités mathématiques (comme en maths !) :
- `*` et `/` sont calculés AVANT `+` et `-`
- Tu peux utiliser des parenthèses `()` pour forcer l'ordre

```python
resultat1 = 2 + 3 * 4      # = 2 + 12 = 14 (multiplication d'abord)
resultat2 = (2 + 3) * 4    # = 5 * 4 = 20 (parenthèses d'abord)
```

### ✏️ Exercice 4 : Fichier `exercice_04.py`

**Comment faire cet exercice :**

1. **Ouvre `exercice_04.py`**
2. **Lis les instructions** dans les commentaires
3. **Crée tes variables** pour les nombres
4. **Fais les calculs** demandés en utilisant `+`, `-`, `*`, `/`
5. **Affiche les résultats** avec `print()`
6. **Teste ton programme** : `python exercice_04.py`

**Exemple de ce que tu pourrais écrire :**
```python
# Calcul de l'aire d'un rectangle
longueur = 10
largeur = 5
aire = longueur * largeur
print(aire)  # Affiche : 50
```

---

## Chapitre 6 : Demander quelque chose à l'utilisateur avec `input()`

Jusqu'ici, nos programmes n'interagissaient pas avec l'utilisateur. Avec `input()`, on peut poser des questions et attendre une réponse !

### 🔍 Comment fonctionne `input()` ?

```python
reponse = input("Comment tu t'appelles ? ")
print("Bonjour", reponse)
```

**Ce qui se passe quand tu lances ce programme :**

| Étape | Ce qui se passe | Ce que tu vois dans le terminal |
|-------|-----------------|--------------------------------|
| 1 | Python affiche la question | `Comment tu t'appelles ? ` |
| 2 | Le programme **s'arrête et attend** que tu tapes quelque chose | Le curseur clignote, tu peux taper |
| 3 | Tu tapes ta réponse (ex: "Lucas") et tu appuies sur **Entrée** | `Comment tu t'appelles ? Lucas` |
| 4 | Ta réponse est rangée dans la variable `reponse` | (rien ne s'affiche) |
| 5 | `print()` affiche le message | `Bonjour Lucas` |

### 💡 Astuce : L'espace à la fin de la question

Regarde bien : `"Comment tu t'appelles ? "` → il y a un **espace avant le guillemet fermant** !

Sans cet espace, le texte tapé par l'utilisateur serait collé à la question :
- ❌ `Comment tu t'appelles ?Lucas` (pas d'espace)
- ✅ `Comment tu t'appelles ? Lucas` (avec espace)

### ⚠️ Attention : `input()` renvoie TOUJOURS du texte !

C'est très important : même si l'utilisateur tape un nombre, `input()` le considère comme du texte !

```python
age = input("Quel âge as-tu ? ")
# Si tu tapes 14, age contient "14" (texte), pas 14 (nombre)
```

**Pourquoi c'est un problème ?**
```python
age = input("Quel âge as-tu ? ")
# L'utilisateur tape 14
age_dans_10_ans = age + 10  # ❌ ERREUR ! On ne peut pas additionner du texte et un nombre
```

### 🔧 Solution : Convertir le texte en nombre

Pour transformer du texte en nombre, utilise `int()` (pour un nombre entier) :

```python
age_texte = input("Quel âge as-tu ? ")   # age_texte = "14" (texte)
age_nombre = int(age_texte)               # age_nombre = 14 (nombre)
age_dans_10_ans = age_nombre + 10         # age_dans_10_ans = 24 ✅
```

**Version raccourcie** (tout sur une ligne) :
```python
age = int(input("Quel âge as-tu ? "))
```

Ce qui se passe :
1. `input(...)` demande l'âge et récupère la réponse en texte ("14")
2. `int(...)` convertit ce texte en nombre (14)
3. Le nombre est rangé dans `age`

### ✏️ Exercice 5 : Fichier `exercice_05.py`

**Comment faire cet exercice :**

1. **Ouvre `exercice_05.py`**
2. **Crée un programme qui :**
   - Demande le prénom de l'utilisateur
   - Demande son âge
   - Affiche un message personnalisé

**Exemple de code :**
```python
prenom = input("Comment tu t'appelles ? ")
age = int(input("Quel âge as-tu ? "))

print("Salut", prenom, "!")
print("Tu as", age, "ans")
print("Dans 10 ans, tu auras", age + 10, "ans")
```

3. **Teste ton programme** : quand tu le lances, tu devras taper des réponses dans le terminal !

---

## Chapitre 7 : Les conditions avec `if`

Parfois, on veut que le programme fasse quelque chose **seulement SI** une condition est vraie. C'est comme dans la vie :
- "**SI** il pleut, **ALORS** je prends mon parapluie"
- "**SI** j'ai fini mes devoirs, **ALORS** je peux jouer"

### 🔍 La structure d'une condition

```python
age = 15

if age >= 13:
    print("Tu es au collège !")
```

**Décortiquons ce code :**

| Élément | C'est quoi ? | Explication |
|---------|--------------|-------------|
| `if` | Le mot-clé | Signifie "SI" en anglais |
| `age >= 13` | La condition | La question qu'on pose (est-ce que age est supérieur ou égal à 13 ?) |
| `:` | Les deux-points | **OBLIGATOIRE !** Ils marquent la fin de la condition |
| `    print(...)` | L'action | Ce qui se passe si la condition est vraie |

### ⚠️ SUPER IMPORTANT : L'indentation (les espaces au début)

Tu as remarqué les espaces avant `print()` ? Ce n'est **PAS** une décoration, c'est **OBLIGATOIRE** !

```python
if age >= 13:
    print("Tu es au collège !")   # ← 4 espaces au début (ou 1 tabulation)
```

**L'indentation** (les espaces au début de la ligne), c'est ce qui dit à Python "cette ligne fait partie du if".

**Comment faire l'indentation :**
- Appuie sur la touche **Tab** (↹) à gauche du clavier (au-dessus de Caps Lock)
- OU tape 4 espaces

**Sans indentation = ERREUR :**
```python
if age >= 13:
print("Tu es au collège !")   # ❌ ERREUR ! Python ne comprend pas
```

### 📊 Les comparaisons

| Symbole | Signification | Comment le taper ? | Exemple |
|---------|---------------|-------------------|---------|
| `==` | égal à | Tape `=` deux fois | `age == 13` |
| `!=` | différent de | `!` puis `=` | `age != 13` |
| `>` | plus grand que | **Maj + <** | `age > 13` |
| `<` | plus petit que | La touche **<** | `age < 13` |
| `>=` | plus grand ou égal | `>` puis `=` | `age >= 13` |
| `<=` | plus petit ou égal | `<` puis `=` | `age <= 13` |

### ⚠️ Attention : `=` vs `==`

C'est une erreur TRÈS fréquente chez les débutants !

| Symbole | Utilisation | Exemple |
|---------|-------------|---------|
| `=` | **Ranger** une valeur dans une variable | `age = 15` (on met 15 dans age) |
| `==` | **Comparer** deux valeurs | `if age == 15:` (est-ce que age vaut 15 ?) |

### 🔀 Le `else` (sinon)

Que faire si la condition est fausse ? On utilise `else` :

```python
age = 10

if age >= 13:
    print("Tu es au collège !")
else:
    print("Tu es à l'école primaire !")
```

**Ce qui se passe :**
1. Python vérifie : est-ce que `10 >= 13` ? → **NON** (c'est faux)
2. Comme c'est faux, Python saute le premier `print()` et exécute ce qui est après `else:`

**Attention :** `else:` a aussi besoin de `:` à la fin et l'action doit être **indentée** !

### 📝 Plusieurs lignes dans un `if`

Tu peux mettre plusieurs actions dans un `if`, il suffit qu'elles soient toutes indentées :

```python
age = 15

if age >= 13:
    print("Tu es au collège !")
    print("Tu as", age, "ans")
    print("Bon courage pour les cours !")

print("Ce message s'affiche toujours")  # ← pas d'indentation = en dehors du if
```

### ✏️ Exercice 6 : Fichier `exercice_06.py`

**Comment faire cet exercice :**

1. **Ouvre `exercice_06.py`**
2. **N'oublie pas :**
   - Les `:` à la fin de `if` et `else`
   - L'**indentation** (touche Tab) pour les lignes à l'intérieur
3. **Teste plusieurs fois** ton programme avec différentes valeurs pour vérifier que les deux cas fonctionnent

---

## Chapitre 8 : Les fonctions - Des recettes réutilisables

Une **fonction**, c'est comme une recette qu'on peut réutiliser plusieurs fois. Au lieu de réécrire le même code encore et encore, tu l'écris UNE fois dans une fonction et tu l'utilises autant de fois que tu veux !

### 🔍 Créer une fonction

```python
def dire_bonjour():
    print("Bonjour !")
    print("Comment vas-tu ?")
```

**Décortiquons ce code :**

| Élément | C'est quoi ? | Explication |
|---------|--------------|-------------|
| `def` | Le mot-clé | Signifie "je définis une fonction" (definition) |
| `dire_bonjour` | Le nom de la fonction | Tu choisis le nom que tu veux (mêmes règles que les variables) |
| `()` | Les parenthèses | Obligatoires ! On y met les paramètres (voir plus bas) |
| `:` | Les deux-points | Marquent la fin de la définition |
| `    print(...)` | Le corps de la fonction | Les actions à effectuer (avec **indentation** !) |

### ⚠️ Créer ≠ Utiliser

**ATTENTION !** Quand tu écris `def dire_bonjour():`, tu **crées** la recette, mais tu ne l'**utilises** pas encore !

```python
# On CRÉE la fonction (on écrit la recette)
def dire_bonjour():
    print("Bonjour !")

# À ce stade, RIEN ne s'affiche encore !

# On UTILISE la fonction (on exécute la recette)
dire_bonjour()    # Maintenant "Bonjour !" s'affiche !
```

### 📞 Appeler (utiliser) une fonction

Pour utiliser une fonction, on écrit son nom suivi de parenthèses :

```python
dire_bonjour()   # ← Les parenthèses sont OBLIGATOIRES !
```

Tu peux l'appeler autant de fois que tu veux :
```python
dire_bonjour()   # Affiche "Bonjour !" et "Comment vas-tu ?"
dire_bonjour()   # Affiche à nouveau "Bonjour !" et "Comment vas-tu ?"
dire_bonjour()   # Et encore une fois !
```

### 📦 Les paramètres : des ingrédients pour ta recette

Un **paramètre**, c'est une variable que tu donnes à la fonction pour qu'elle l'utilise :

```python
def dire_bonjour(prenom):
    print("Bonjour", prenom, "!")

dire_bonjour("Marie")  # Affiche : Bonjour Marie !
dire_bonjour("Lucas")  # Affiche : Bonjour Lucas !
```

**Ce qui se passe :**
1. Quand on appelle `dire_bonjour("Marie")`, Python met `"Marie"` dans la variable `prenom`
2. La fonction utilise `prenom` dans son `print()`
3. Résultat : "Bonjour Marie !"

**Plusieurs paramètres :**
```python
def presenter(prenom, age):
    print("Je m'appelle", prenom)
    print("J'ai", age, "ans")

presenter("Lucas", 14)
# Affiche :
# Je m'appelle Lucas
# J'ai 14 ans
```

### ⚠️ Erreurs fréquentes

| Erreur | Problème | Solution |
|--------|----------|----------|
| `dire_bonjour` (sans parenthèses) | La fonction n'est pas appelée | Ajoute les parenthèses : `dire_bonjour()` |
| Pas d'indentation dans le corps | Python ne sait pas ce qui fait partie de la fonction | Utilise **Tab** pour indenter |
| Oublier les `:` | Erreur de syntaxe | Ajoute `:` après les parenthèses |

### ✏️ Exercice 7 : Fichier `exercice_07.py`

**Comment faire cet exercice :**

1. **Ouvre `exercice_07.py`**
2. **Crée une fonction** avec `def nom_fonction():`
3. **N'oublie pas** l'indentation pour le corps de la fonction
4. **Appelle ta fonction** après l'avoir créée
5. **Teste** avec `python exercice_07.py`

**Exemple complet :**
```python
# Je crée ma fonction
def saluer(nom):
    print("Salut", nom, "!")
    print("Bienvenue dans mon programme !")

# Je l'utilise
saluer("Alice")
saluer("Bob")
```

---

## Chapitre 9 : Les fonctions qui renvoient une valeur

Jusqu'ici, nos fonctions faisaient des `print()`. Mais parfois, on veut qu'une fonction **calcule** quelque chose et nous **donne le résultat** pour l'utiliser plus tard. C'est le rôle de `return` !

### 🔍 `print()` vs `return` : quelle différence ?

| `print()` | `return` |
|-----------|----------|
| **Affiche** quelque chose à l'écran | **Renvoie** une valeur au programme |
| On voit le résultat, mais on ne peut pas l'utiliser | On peut stocker le résultat dans une variable |
| La fonction continue après le print | La fonction **s'arrête** immédiatement après le return |

**Exemple pour comprendre :**

```python
# Avec print : on VOIT le résultat, mais on ne peut pas l'utiliser
def addition_print(a, b):
    print(a + b)

addition_print(5, 3)  # Affiche 8
# Mais impossible de faire quelque chose avec ce 8...

# Avec return : on RÉCUPÈRE le résultat pour l'utiliser
def addition_return(a, b):
    return a + b

resultat = addition_return(5, 3)  # resultat contient 8
print(resultat)                    # Affiche 8
print(resultat * 2)                # Affiche 16 (on peut l'utiliser !)
```

### 🔍 Comment fonctionne `return` ?

```python
def additionner(a, b):
    resultat = a + b
    return resultat

somme = additionner(5, 3)
print(somme)  # Affiche : 8
```

**Ce qui se passe étape par étape :**

| Étape | Ce qui se passe |
|-------|-----------------|
| 1 | On appelle `additionner(5, 3)` → `a = 5` et `b = 3` |
| 2 | La fonction calcule `resultat = 5 + 3` → `resultat = 8` |
| 3 | `return resultat` renvoie la valeur `8` |
| 4 | Cette valeur `8` est stockée dans `somme` |
| 5 | On affiche `somme` → 8 |

C'est comme une **machine** : on met des ingrédients (5 et 3), elle fait son travail, et elle nous **donne** le résultat (8).

### 💡 Version raccourcie

Tu peux écrire le calcul directement dans le `return` :

```python
def additionner(a, b):
    return a + b    # Plus court, même résultat !
```

### 📝 Utiliser le résultat d'une fonction

Une fois que la fonction renvoie une valeur, tu peux :

**1. La stocker dans une variable :**
```python
resultat = additionner(5, 3)
print(resultat)  # 8
```

**2. L'utiliser directement dans un print :**
```python
print(additionner(5, 3))  # Affiche 8 directement
```

**3. L'utiliser dans un calcul :**
```python
total = additionner(5, 3) + additionner(10, 2)
print(total)  # 8 + 12 = 20
```

**4. L'utiliser dans une condition :**
```python
if additionner(5, 3) > 10:
    print("C'est plus grand que 10")
else:
    print("C'est 10 ou moins")
```

### ⚠️ Attention : `return` arrête la fonction !

Tout ce qui est écrit **après** le `return` ne sera **jamais exécuté** :

```python
def exemple():
    return 5
    print("Ce message ne s'affichera JAMAIS")  # ← Code inaccessible !
```

### ✏️ Exercice 8 : Fichier `exercice_08.py`

**Comment faire cet exercice :**

1. **Ouvre `exercice_08.py`**
2. **Crée des fonctions** qui font des calculs
3. **Utilise `return`** pour renvoyer le résultat (pas `print()` !)
4. **Récupère le résultat** dans une variable
5. **Affiche** le résultat avec `print()`

**Exemple :**
```python
def calculer_double(nombre):
    return nombre * 2

# Utilisation
mon_nombre = 7
resultat = calculer_double(mon_nombre)
print("Le double de", mon_nombre, "est", resultat)
```

---

## 🎮 Projet Final : Fichier `projet_final.py`

**Bravo !** Tu as appris les bases de Python ! Pour terminer, tu vas créer un petit jeu en utilisant **tout ce que tu as appris**.

### 🎯 Le projet : Jeu de devinette

Tu vas créer un jeu où l'ordinateur choisit un nombre secret et le joueur doit le deviner !

### 📋 Ce que tu vas utiliser

| Concept | Comment tu vas l'utiliser |
|---------|--------------------------|
| `print()` | Pour afficher les messages au joueur |
| Variables | Pour stocker le nombre secret et les essais du joueur |
| `input()` | Pour demander au joueur de deviner |
| `int()` | Pour convertir la réponse en nombre |
| `if/else` | Pour dire si c'est gagné, trop grand ou trop petit |
| Fonctions | Pour organiser ton code proprement |

### 💡 Conseils pour réussir

1. **Commence simple** : fais d'abord une version basique qui fonctionne
2. **Teste souvent** : lance ton programme après chaque modification
3. **Lis les erreurs** : elles t'indiquent où est le problème
4. **N'abandonne pas** : c'est normal de faire des erreurs, c'est comme ça qu'on apprend !

### 🏆 Pour aller plus loin (bonus)

Si tu termines en avance, tu peux améliorer ton jeu :
- Compter le nombre d'essais
- Limiter le nombre de tentatives
- Ajouter un système de score
- Permettre de rejouer sans relancer le programme

---

## 📝 Aide-mémoire

### 🖨️ Afficher du texte
```python
print("Bonjour")                    # Affiche : Bonjour
print("J'ai", 14, "ans")            # Affiche : J'ai 14 ans
```

### 📦 Variables
```python
nom = "Lucas"      # Texte (str) → avec guillemets
age = 13           # Nombre entier (int) → sans guillemets
taille = 1.65      # Nombre décimal (float) → avec un point
actif = True       # Booléen (bool) → True ou False
```

### ⌨️ Demander à l'utilisateur
```python
reponse = input("Ta question ? ")           # Récupère du texte
nombre = int(input("Un nombre ? "))          # Récupère un nombre entier
```

### 🔢 Calculs
```python
resultat = 5 + 3    # Addition → 8
resultat = 5 - 3    # Soustraction → 2
resultat = 5 * 3    # Multiplication → 15
resultat = 6 / 2    # Division → 3.0
```

### ❓ Conditions
```python
if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

**Les comparaisons :** `==` (égal), `!=` (différent), `>`, `<`, `>=`, `<=`

### 🔧 Fonctions
```python
# Fonction simple
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()    # Appel de la fonction

# Fonction avec paramètre
def saluer(prenom):
    print("Salut", prenom)

saluer("Marie")   # Affiche : Salut Marie

# Fonction qui renvoie une valeur
def double(n):
    return n * 2

resultat = double(5)   # resultat = 10
```

### ⌨️ Raccourcis VS Code à retenir

| Raccourci | Action |
|-----------|--------|
| **Ctrl + S** | Sauvegarder le fichier |
| **Ctrl + ù** | Ouvrir/fermer le terminal |
| **Ctrl + Z** | Annuler la dernière action |
| **Tab** | Ajouter une indentation |

---

**Bon courage et amuse-toi bien ! 🚀**

*N'oublie pas : faire des erreurs, c'est normal ! Chaque erreur est une occasion d'apprendre. Les meilleurs programmeurs sont ceux qui ont fait le plus d'erreurs et qui ont appris de chacune d'elles.*
