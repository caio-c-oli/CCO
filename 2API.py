#importar biblioteca
from flask import Flask,jsonify

#Iniciar a aplicação
app = Flask(__name__)

#criar uma rota
@app.route('/')
def main():
    return jsonify(aluno='Caio')

if __name__ == '__main__':
    app.run(debug=True) #Executar a aplicação 