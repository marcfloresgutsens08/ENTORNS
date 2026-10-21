
| Endpoint | Método HTTP | Función |
|---|---|---|
| `/auth/register` | `GET` | Muestra el formulario de registro. |
| `/auth/register` | `POST` | Registra un usuario nuevo. |
| `/auth/login` | `GET` | Muestra el formulario de inicio de sesión. |
| `/auth/login` | `POST` | Comprueba las credenciales e inicia sesión. |
| `/auth/logout` | `GET` | Cierra la sesión del usuario. |
| `/hello` | `GET` | Devuelve el texto "Hello, World!". |
| `/` | `GET` | Muestra todas las publicaciones, ordenadas de más recientes a más antiguas. |
| `/create` | `GET` | Muestra el formulario para crear una publicación. |
| `/create` | `POST` | Crea una publicación nueva. |
| `/<int:id>/update` | `GET` | Muestra el formulario para editar una publicación. |
| `/<int:id>/update` | `POST` | Guarda los cambios de una publicación. |
| `/<int:id>/delete` | `POST` | Elimina una publicación. |