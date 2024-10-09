from app import app
from flask import render_template
from flask import request
import requests
import json
link = "https://flasktintester-default-rtdb.firebaseio.com/"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titulo="Página inicial")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="contato")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="cadastro")

@app.route('/cadastrarUsuario', methods=['POST'])
def cadatrarUsuario():
    try:
        cpf = request.form.get("cpf")
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        dados = {"cpf":cpf, "nome":nome, "telefone":telefone, "endereco":endereco}
        requesicao = requests.post(f'{link}/cadastro/.json', data = json.dumps(dados))
        return 'cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n + {e}'

@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        return dicionario

    except Exception as e:
        return f'Algo deu errado\n +{e}'

@app.route('/listarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json') #solicitando
        dicionario = requisicao.json()
        idCadastro = "" #coletar o id
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == '1546468':
                idCadastro = codigo
                return idCadastro
    except Exception as e:
        return f'Algo deu errado \n {e}'

@app.route('/atualizar')
def atualizar():
    try:
        dados = {"nome":"João"}
        requisicao = requests.patch(f'{link}/cadastro/-O8miKUUwIzpK5PxTx2Q/.json', data=json.dumps(dados)) #atualizar
        return "Atualizado com sucesso!"
    except Exception as e:
        return f'Algo deu errado \n {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastro/-O8miKUUwIzpK5PxTx2Q/.json')
        return "Excluído com sucesso!"
    except Exception as e:
        return f'Algo deu errado\n {e}'