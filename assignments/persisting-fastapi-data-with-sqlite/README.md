# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Upgrade a FastAPI book API to store its data in SQLite instead of memory. Practice creating a database table, running SQL from API routes, and confirming that records remain available after the server restarts.

## 📝 Tasks

### 🛠️ Create the SQLite Database

#### Description
Start with the provided working in-memory book API. Create a SQLite database file and a `books` table with columns for each book's ID, title, and author.

#### Requirements
Completed program should:

- Use Python's built-in `sqlite3` module and create a database file named `books.db`
- Create the `books` table automatically when the application starts, without deleting existing records
- Use an integer primary key for each book ID and store the title and author as text


### 🛠️ Connect the API Routes to SQLite

#### Description
Replace the in-memory dictionary operations with SQL queries so that every book endpoint reads and changes database records.

#### Requirements
Completed program should:

- Update `GET /books` and `GET /books/{book_id}` to read books from SQLite
- Update `POST /books` to insert a book and return its generated ID, title, and author
- Update `PUT /books/{book_id}` and `DELETE /books/{book_id}` to change or remove database records
- Use parameterized SQL queries for values supplied by a request
- Preserve the API's existing response formats and return `404 Not Found` when an update, delete, or lookup targets a missing book


### 🛠️ Verify Data Persists Between Restarts

#### Description
Run the API, create and retrieve a book, then restart the server and retrieve the same book again.

#### Requirements
Completed program should:

- Start the API with `uvicorn starter-code:app --reload` and use `/docs` to test the endpoints
- Confirm that a book created before the restart can still be retrieved afterward
- Confirm that updating or deleting a book changes the stored record and that a deleted book is no longer returned
