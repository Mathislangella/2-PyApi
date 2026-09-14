# TP 1 — Créer sa première API avec FastAPI

Durée indicative : 2h30. Vous avancez à votre rythme, ce n'est pas un chrono strict.

## Avant de commencer

Vous n'avez jamais utilisé ni Python en ligne de commande ni FastAPI ? Pas de souci, suivez chaque commande une par une, dans l'ordre. Si une commande ne marche pas, ne passez pas à la suivante : réglez le problème d'abord (ou appelez-moi).

Ouvrez un terminal dans le dossier de votre projet (celui où vous voulez travailler).

---

## Étape 0 — Installer l'environnement (15 min)

### 1. Créer l'environnement virtuel

Un environnement virtuel isole les librairies de ce projet du reste de votre ordinateur. C'est une bonne pratique à prendre dès maintenant.

**Mac / Linux / Ubuntu :**
```bash
python3 -m venv venv
```

**Windows :**
```bash
python -m venv venv
```
*(si `python` ne fonctionne pas, essayez `py -m venv venv`)*

### 2. Activer l'environnement virtuel

**Mac / Linux / Ubuntu (terminal classique) :**
```bash
source venv/bin/activate
```

**Windows — PowerShell :**
```powershell
.\venv\Scripts\Activate.ps1
```
> Si vous avez une erreur "l'exécution de scripts est désactivée", tapez d'abord une fois :
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> puis relancez la commande d'activation.

**Windows — Invite de commandes (cmd) :**
```cmd
venv\Scripts\activate.bat
```

**Windows — Git Bash :**
```bash
source venv/Scripts/activate
```

✅ **Vérification** : votre invite de terminal doit maintenant afficher `(venv)` au début de la ligne. Si ce n'est pas le cas, l'activation n'a pas fonctionné, recommencez.

### 3. Installer FastAPI et uvicorn

```bash
pip install fastapi uvicorn
```

FastAPI est le framework qu'on utilise pour construire l'API. Uvicorn est le serveur qui fait réellement tourner votre application (FastAPI seul ne peut pas se lancer).

### 4. Créer le fichier principal du projet

**Mac / Linux / Ubuntu :**
```bash
touch main.py
```

**Windows — PowerShell :**
```powershell
New-Item main.py
```

**Windows — Invite de commandes (cmd) :**
```cmd
type nul > main.py
```

**Ou, plus simple, quel que soit votre système** : créez le fichier directement depuis votre éditeur de code (VS Code, PyCharm...) — clic droit dans l'explorateur de fichiers → "Nouveau fichier" → nommez-le `main.py`.

### 5. Écrire le tout premier code

Ouvrez `main.py` dans votre éditeur et copiez ce code exactement :

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

Enregistrez le fichier.

### 6. Lancer le serveur

```bash
uvicorn main:app --reload
```

✅ **Vérification** : vous devez voir apparaître une ligne du type `Uvicorn running on http://127.0.0.1:8000`. Ouvrez cette adresse dans votre navigateur : vous devez voir `{"message":"Hello World"}`.

⚠️ Le `--reload` permet au serveur de redémarrer automatiquement à chaque fois que vous modifiez et enregistrez `main.py`. Laissez-le tourner dans ce terminal, et ouvrez un **nouveau terminal** (ou un nouvel onglet) si vous avez besoin de taper d'autres commandes — n'arrêtez pas le serveur entre chaque étape.

---

## Étape 1 — Vos premières routes GET (30 min)

**Objectif** : choisir un thème et créer vos premières routes qui renvoient des données.

1. Choisissez un thème pour votre API (une bibliothèque, des films, des recettes, des jeux vidéo... ce que vous voulez) et listez 2 ressources différentes (ex : des livres et des auteurs).

2. Créez une route `GET` qui renvoie une liste fixe pour votre première ressource. Exemple avec des livres :
```python
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "Le Petit Prince", "author": "Antoine de Saint-Exupéry"},
]

@app.get("/books")
def get_books():
    return books
```

3. Ajoutez une route `GET` avec un paramètre dynamique dans l'URL, pour récupérer un seul élément :
```python
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Livre non trouvé"}
```

4. Testez vos routes dans le navigateur, ou mieux, via la documentation automatique à l'adresse `http://127.0.0.1:8000/docs`.

---

## Étape 2 — Paramètres et création, POST (40 min)

**Objectif** : pouvoir ajouter de nouveaux éléments à vos ressources.

1. Ajoutez une route `POST` pour créer un nouvel élément sur votre première ressource :
```python
@app.post("/books")
def create_book(book: dict):
    books.append(book)
    return book
```

2. Vérifiez que l'élément que vous venez de créer apparaît bien quand vous refaites `GET /books` (via `/docs`, cliquez sur "Try it out" pour tester directement dans le navigateur).

3. Faites la même chose pour votre deuxième ressource (une liste, une route GET liste, une route GET détail, une route POST).

---

## Étape 3 — Étoffer une ressource (30 min)

**Objectif** : avoir des données plus réalistes.

1. Choisissez une de vos deux ressources et ajoutez 5 à 6 éléments minimum dans la liste de départ (pas juste 1 ou 2).

2. Vérifiez que chaque champ a un type cohérent (un nombre reste un nombre, un texte reste un texte).

3. **Si vous avez le temps** : essayez une URL avec deux paramètres imbriqués, par exemple `/books/{book_id}/reviews` pour les avis d'un livre en particulier.

---

## Étape 4 — Vérifier avec Swagger (20 min)

**Objectif** : tester votre API dans son ensemble, comme si vous étiez quelqu'un d'extérieur.

1. Ouvrez `http://127.0.0.1:8000/docs` et testez chacune de vos routes avec le bouton "Try it out".

2. Vérifiez que les noms de vos routes et de vos paramètres sont compréhensibles pour quelqu'un qui découvrirait votre API pour la première fois.

3. Repérez une route qui pourrait mal se comporter (par exemple : que se passe-t-il si vous demandez `/books/999` et que ce livre n'existe pas ?). On ne corrige pas ça aujourd'hui, on y reviendra en séance 3 avec la validation des données.

---

## Étape 5 — Bonus, si vous avez terminé (15 min)

Ces points ne sont pas obligatoires, à faire uniquement si tout le reste fonctionne :

- Ajoutez une route `DELETE` sur une de vos ressources
- Ajoutez un paramètre optionnel sur une route GET (par exemple filtrer les livres par auteur)
- Essayez de changer le type attendu d'un paramètre (`int` en `str`) et observez comment FastAPI réagit

---

## Contrainte minimale à respecter

À la fin du TP, votre API doit avoir :
- ✅ Au moins **2 ressources** différentes
- ✅ Au moins une route **GET** (liste) et une route **GET** (détail avec paramètre) par ressource
- ✅ Au moins une route **POST** par ressource
- ✅ Toutes les routes testées et fonctionnelles via `/docs`

## En cas de blocage

Appelez-moi dès que vous êtes bloqué plus de 5 minutes sur quelque chose, pas la peine de rester coincé seul dans votre coin.