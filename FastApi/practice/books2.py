from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status


app = FastAPI()

class Book:
    id:int
    title:str 
    author:str
    description:str
    rating:int
    published_date:int

    def __init__(self,id,title,author,description,rating,published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: int | None = Field(description="ID is not needed on create",default=None)
    title:str = Field(min_length=3)
    author:str = Field(min_length=1)
    description:str = Field(min_length=1, max_length=100)
    rating:int = Field(gt=1, lt=6)
    published_date:int = Field(min_length=4)

    model_config = {
        "json_schema_extra":{
            "example":{
                "title":"A new Title",
                "author":"New Author",
                "description":"A New Description",
                "rating":5,
                "published_date":2029
            }
        }
    }


BOOKS = [
         Book(1, 'CS Pro 1','coding with roby 1','A nice book 1',5,2012),
         Book(2, 'CS Pro 2','coding with roby 2','A nice book 2',5,2013),
         Book(3, 'CS Pro 3','coding with roby 3','A nice book 3',5,2014),
         Book(4, 'CS Pro 4','coding with roby 4','A nice book 4',5,2015),
         Book(5, 'CS Pro 5','coding with roby 5','A nice book 5',5,2016),
         Book(6, 'CS Pro 6','coding with roby 6','A nice book 6',5,2017)
         ]

@app.get("/books", status_code = status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}",status_code = status.HTTP_200_OK)
async def read_book(book_id:int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404,detail='Item Not Found!')    
        
@app.get("/books/",status_code = status.HTTP_200_OK)
async def read_book_by_rating(rating: int = Query(gt=0, lt=6)):
    book_to_return = []
    for book in BOOKS:
        if book.rating == rating:
            book_to_return.append(book)
    return book_to_return      

@app.get('/books/book_date/',status_code = status.HTTP_200_OK)
async def book_by_published_date(date:int = Query(gt=1990,lt=2049)):
    Books = []
    for book in BOOKS:
        if book.published_date == date:
            Books.append(book)
    return Books    

                    

@app.post("/create-book",status_code = status.HTTP_201_CREATED)
async def create_book(book : BookRequest):
    new_book = Book(**book.model_dump())
    # print(type(new_book))
    BOOKS.append(find_book_id(new_book))

def find_book_id(book:Book):
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1

    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    return book            


@app.put("/books/update_book",status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True  
            break      
            
    if not book_changed:
        raise HTTPException(status_code=404,detail='Item Not Found!')        

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break     
        
        if not book_changed:
           raise HTTPException(status_code=404,detail='Item Not Found!')                