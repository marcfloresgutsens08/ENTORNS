from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello():
    return "¡Hola Mundo!"

@app.route("/dam1")
def dam1():
    return "¡Hola DAM!"


@app.route('/suma/<int:s1>/<int:s2>',methods=['GET'])
def suma(s1,s2):
    return str(s1+s2)

if __name__ == "__main__":
    app.run()