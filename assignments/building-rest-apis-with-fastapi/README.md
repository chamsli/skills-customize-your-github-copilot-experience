# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for managing books with FastAPI. Practice defining routes, accepting validated request data, using HTTP methods and status codes, and handling missing resources.

## 📝 Tasks

### 🛠️ Create Routes to Read Books

#### Description
Use the provided starter code to build the read operations for a small in-memory book collection. Each book has an `id`, `title`, and `author`.

#### Requirements
Completed program should:

- Add `GET /books` to return all books as a JSON list
- Add `GET /books/{book_id}` to return one book by its ID
- Return HTTP `404 Not Found` when the requested book ID does not exist


### 🛠️ Add Books to the Collection

#### Description
Add an endpoint that lets a client create a book by sending JSON data. Let FastAPI and the provided Pydantic model validate the request body.

#### Requirements
Completed program should:

- Add `POST /books` that accepts a book's `title` and `author` using the `BookInput` model
- Assign each new book a unique ID and save it in the in-memory `books` collection
- Return the created book with HTTP `201 Created`


### 🛠️ Update and Delete Books

#### Description
Complete the API with operations for replacing a book's details and deleting a book from the collection.

#### Requirements
Completed program should:

- Add `PUT /books/{book_id}` to replace a book's title and author using `BookInput`, and return the updated book
- Add `DELETE /books/{book_id}` to remove a book and return HTTP `204 No Content`
- Return HTTP `404 Not Found` when either operation targets a book ID that does not exist
- Run the API with `uvicorn starter-code:app --reload` and use the interactive documentation at `/docs` to try each operation
