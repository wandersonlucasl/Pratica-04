from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, template_folder='templates')
from utils import valida_cadastro

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/ver')
def ver():
    return render_template('ver-aluno.html')

@app.route('/editar')
def editar():
    return render_template('editar.html')

@app.route('/excluir')
def excluir():
    return render_template('excluir.html')

@app.route('/listar')
def listar():
    return render_template('listar.html')

if __name__ == '__main__':
    app.run(debug=True)   