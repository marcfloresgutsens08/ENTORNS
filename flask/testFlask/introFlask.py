from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola Mundo!"

@app.route("/dam1")
def dam1():
    return "Estem a DAM!"

@app.route('/suma/<int:s1>/<int:s2>',methods=['GET'])
def suma(s1,s2):
    return str(s1+s2)

if __name__ == "__main__":
    app.run()   
