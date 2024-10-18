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

@app.route('/atualizacao')
def atualizacao():
    return render_template('atualizacao.html', titulo="atualizar")

@app.route('/deletar')
def deletar():
    return render_template('deletar.html', titulo="excluir cadastro")


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

        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == '1546468':
                idCadastro = codigo
                return idCadastro
    except Exception as e:
        return f'Algo deu errado \n {e}'


@app.route('/atualizar', methods=['POST'])
def atualizar():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        cpf = request.form.get("cpf")
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        dados = {"cpf": cpf, "nome": nome, "telefone": telefone, "endereco": endereco}
        for codigo in dicionario:
                chave = dicionario[codigo]['cpf']
                if chave == cpf:
                    requisicao = requests.patch(f'{link}/cadastro/{codigo}/.json', data=json.dumps(dados))
                    return "Atualizado com sucesso!"
    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/excluir', methods=['POST'])
def excluir():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        cpf = request.form.get("cpf")
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == cpf:
                requisicao = requests.delete(f'{link}/cadastro/{codigo}/.json')
        return "Excluído com sucesso!"
    except Exception as e:
        return f'Algo deu errado\n {e}'