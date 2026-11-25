# Mapa de peticions Http (GET / POST) 
| Endpoint      | Mètodes   | Descripció |
|---------------|-----------|------------|
| auth.login    | GET, POST | Mostra el formulari d'inici de sessió i valida les credencials de l'usuari |
| auth.logout   | GET       | Tanca la sessió de l'usuari actual                |
| auth.register | GET, POST | Mostra el formulari de registre i crea un usuari nou |
| blog.create   | GET, POST | Mostra el formulari per crear una publicació nova i la desa |
| blog.delete   | POST      | Elimina la publicació amb l'identificador indicat |
| blog.index    | GET       | Mostra el llistat de totes les publicacions       |
| blog.update   | GET, POST | Mostra el formulari per editar una publicació i desa els canvis |
| hello         | GET       | Pàgina de prova que mostra un missatge de salutació |
| index         | GET       | Pàgina principal de l'aplicació                   |
| static        | GET       | Serveix els fitxers estàtics (CSS, imatges, JS)   |
