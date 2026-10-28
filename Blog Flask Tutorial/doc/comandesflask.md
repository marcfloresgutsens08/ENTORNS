# Comandes Flask

Els noms envoltats de doble guió baix (com \_\_init\_\_.py, \_\_main\_\_.py o mètodes com \_\_init\_\_()) són paraules reservades de Python

- \_\_init\_\_.py (Especial): S'executa automàticament en el moment que algun fitxer del teu projecte fa import flaskr o quan s'invoca el paquet.

Mostra opcions i comandes de l'ordre Flask 

```bash
$ flask --help
```

## Inicialitza la BBDD
```bash
$ flask --app flaskr init-db
```

Què fa exactament aquesta comanda?
- flask: Invoca la interfície de línia d'ordres (CLI) de Flask.
- --app flaskr: Li indica a Flask quina és la teva aplicació o paquet principal (en aquest cas, la carpeta/mòdul flaskr).
- init-db: Executa un mètode/comanda personalitzada (habitualment definida a db.py mitjançant @click.command('init-db')) que s'encarrega d'inicialitzar la base de dades (crear les taules definides en un fitxer schema.sql).

Arrenca l'aplicació.
Com arrenca Flask les aplicacions? https://flask.palletsprojects.com/es/stable/quickstart/


## Inicialitzar l'Aplicació 

```bash
$ flask --app flaskr run --debug
```

S'executa el create_app() de \_\_init\_\_.py

```Python
# flaskr/__init__.py

def create_app():
    app = Flask(__name__)
    # configuració i rutes...
    return app
```

- flask: Invoca l'eina de línia de comandes de Flask.
- --app flaskr: Indica a Flask quina aplicació ha d'executar. En aquest cas, busca el mòdul o paquet anomenat flaskr (sovint utilitzat en el tutorial oficial de Flask).
- run: Arrenca el servidor web local de desenvolupament (per defecte disponible a [http://127.0.0.1:5000/](http://127.0.0.1:5000/)).
- --debug: Activa el mode de depuració (debug mode). Això ofereix dues opcions molt útils durant el desenvolupament: