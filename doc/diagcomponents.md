# Diagrama de Components

Descriure tots els components de l'aplicació

Components : db , _init_ , auth, blog 

## db 

Descripció : funcions d'accés a BBDD
Mètodes : 
- getdb() : Retorna connexió : Mètode que retorna la connexió a BBDD
- close_db()  : Tanca la connexió a BBDD
...


## Diagrama d'arrencada de l'aplicació 

```mermaid

classDiagram
    direction TB

    class auth {
        <<Blueprint>>
        +register() : View
        +login() : View
        +logout() : View
        +load_logged_in_user() : Function
        +login_required(view) : Decorator
    }

    class blog {
        <<Blueprint>>
        +index() : View
        +create() : View
        +update(id) : View
        +delete(id) : View
        +get_post(id, check_author) : Post
    }

    class db {
        <<Mòdul>>
        +get_db() : sqlite3.Connection
        +close_db(e) : None
        +init_db() : None
        +init_db_command() : CLI Command
    }

    class User {
        +INTEGER id PK
        +TEXT username UNIQUE
        +TEXT password
    }

    class Post {
        +INTEGER id PK
        +INTEGER author_id FK
        +TIMESTAMP created 
        +TEXT title
        +TEXT body
    }

    auth --> db
    blog --> db
    Post --> User :
    blog ..> Post : "utilitza / modifica"

    ``` 

