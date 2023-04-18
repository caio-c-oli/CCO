#importar biblioteca
from flask import Flask

#Iniciar a aplicação
app = Flask(__name__)

#criar uma rota
@app.route('/api')
def main():
    return 'Hello Word! Meu site em Flask :D'

if __name__ == '__main__':
    app.run(debug=True) #Executar a aplicação 