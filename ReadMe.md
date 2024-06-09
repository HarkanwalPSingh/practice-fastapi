# Mock Book Collection
Create a REST API for managing a book collection. 
The API should support basic CRUD (Create, Read, Update, Delete) 
operations for books.

## How to run
```shell
docker compose up --build
```

Visit [localhost docs](http://localhost:8000/docs)

## Functional Requirements
- Create User
- Fetch User
- Create Book
- Create Collection
- Update Collection
- Remove Collection

## Out of Scope
- Update/Delete User
- User Auth
- Misc CRUD Operations

## Models
```yaml
User:
  id: Int
  name: String
  emailId: String

Collection:
  id: Int
  userId: Int # Foreign Key
  name: String

Book:
  id: Int
  name: String
  author: String | User
  collectionId: Int # Foreign Key
```

## API Design
### User
**Create User**

POST - ``/user``

BODY
```json
{
  "name": "Harshil",
  "email": "harshil@gmail.com"
}
```

RESPONSE - 200 OK
```json
{
  "id": 1,
  "name": "Harshil",
  "email": "harshil@gmail.com"
}
```

**Fetch User**

GET - ``/user``

PARAM - ``email_id``

RESPONSE - 200 OK
```json
{
  "id": 1,
  "name": "Harshil",
  "email": "harshil@gmail.com"
}
```




