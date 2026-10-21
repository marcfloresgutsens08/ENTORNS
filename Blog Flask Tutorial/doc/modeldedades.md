# Model de dades

## Model Entitat Relació E/R

```mermaid
erDiagram
    user || --o{ Post : id
    user{
        int id
        string username
        string password
    }
    Post {
        date created
        string title
        string body
    }
```

Quin tipus de Base de dades utilitza l'aplicació?


