from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title":"Title One","author":"Author One","category":"Science"},
    {"title":"Title Two","author":"Author Two","category":"Science"},
    {"title":"Title Three","author":"Author Three","category":"History"},
    {"title":"Title Four","author":"Author Four","category":"Math"},
    {"title":"Title Five","author":"Author Five","category":"Math"},
    {"title":"Title Six","author":"Author Six","category":"Math"}
]


@app.get("/books/") # url: http://127.0.0.1:8000/api-endpoint
async def read_category_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
             books_to_return.append(book)

    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author:str, category:str):
    books_to_return = []
    for book in BOOKS: 
        if book.get('author').casefold() == book_author.casefold() and \
           book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return             

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put('/books/update_book')
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book    

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break            