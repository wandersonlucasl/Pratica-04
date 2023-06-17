from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')

banalunos = []

@app.route('/')
def home():
    return render_template('index.html', titulo_pagina="Página inicial")

@app.route('/listar')
def listar():
    return render_template('listar.html', alunos=banalunos, titulo_pagina="Alunos Cadastrados")

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        curso = request.form['curso']
        turno = request.form['turno']
        novo_aluno = {"id": len(banalunos) + 1, "nome": nome, "curso": curso, "turno": turno}
        banalunos.append(novo_aluno)
        return redirect('/listar')
    return render_template('cadastrar.html', titulo_pagina="Cadastrar Aluno")

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    aluno = next((aluno for aluno in banalunos if aluno['id'] == id), None)
    if request.method == 'POST':
        if aluno:
            aluno['nome'] = request.form['nome']
            aluno['curso'] = request.form['curso']
            aluno['turno'] = request.form['turno']
            return redirect('/listar')
        else:
            return "Time não encontrado."
    return render_template('editar.html', aluno=aluno, titulo_pagina="Editar Aluno")

@app.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    aluno = next((aluno for aluno in banalunos if aluno['id'] == id), None)
    if aluno:
        banalunos.remove(aluno)
        return redirect('/listar')
    else:
        return "Time não encontrado."
    
if __name__ == '__main__':
    app.run(debug=True)
