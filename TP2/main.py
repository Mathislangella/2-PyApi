from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "Le Petit Prince", "author": "Antoine de Saint-Exupéry", "year": 1943},
    {"id": 3, "title": "Harry Potter", "author": "J.K. Rowling", "year": 1997},
    {"id": 4, "title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"id": 5, "title": "L'Assommoir", "author": "Zola", "year": 1877},
    {"id": 6, "title": "Le Seigneur des Anneaux", "author": "J.R.R. Tolkien", "year": 1954},
]

users = [
    {"id": 1, "name": "All1", "email": "alice@example.com"},
    {"id": 2, "name": "Alex", "email": "bob@example.com"},
    {"id": 3, "name": "Aller", "email": "charlie@example.com"},
]

@app.get("/")
def root():
    return {"message": "API FastAPI opérationnelle"}

# Create
@app.post("/books")
def create_book(book: dict):
    books.append(book)
    return book


@app.post("/users")
def create_user(user: dict):
    users.append(user)
    return user


# Read
@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "Utilisateur non trouvé"}


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Livre non trouvé"}


# Update
@app.patch("/books/{book_id}")
def update_book(book_id: int, changes: dict):
    for book in books:
        if book["id"] == book_id:
            book.update(changes)
            return book
    return {"error": "Livre non trouvé"}


# Delete
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    global books
    books = [book for book in books if book["id"] != book_id]
    return {"message": "Livre supprimé"}