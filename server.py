from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os
from models import Empresa, Contato, Proposta, Visita, Imagem, Revisao, Tratativa
from database import database
from waitress import serve
from dotenv import load_dotenv
import time
import threading
from tester import ping_service
load_dotenv()


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

secret_key = os.getenv("JWT_SECRET_KEY")
app.config['JWT_SECRET_KEY'] = secret_key
jwt = JWTManager(app)

# Configurar a pasta de upload
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Garantir que a pasta de upload exista
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
    
# Iniciar a thread de ping


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = data.get('usuario')
    senha = data.get('senha')
    
    usuarios = database.get_database().usuarios
    user = usuarios.find_one({"usuario": usuario, "senha": senha})
    
    if user:
        access_token = create_access_token(identity={'usuario': usuario})
        return jsonify({"success": True, "token": access_token})
    else:
        return jsonify({"success": False, "message": "Nome de usuário ou senha incorretos."}), 401


@app.route('/listar_todas_empresas', methods=['GET'])
@jwt_required()
def listar_todas_empresas_route():
    empresas = Empresa.listar_todas()
    return jsonify(empresas)

@app.route('/listar_empresa_por_cnpj', methods=['GET'])
@jwt_required()
def listar_empresa_por_cnpj_route():
    cnpj = request.args.get('cnpj')
    empresa = Empresa.buscar_por_cnpj(cnpj)
    return jsonify(empresa)

@app.route('/cadastrar_empresa', methods=['POST'])
@jwt_required()
def cadastrar_empresa_route():
    valores = request.json
    empresa = Empresa(**valores)
    empresa.inserir_empresa()
    return jsonify({"message": "Empresa cadastrada com sucesso!"})

@app.route('/listar_empresas_por_regiao', methods=['GET'])
@jwt_required()
def listar_empresas_por_regiao():
    regiao = request.args.get('regiao')
    if regiao:
        empresas = Empresa.buscar_por_regiao(regiao)
        return jsonify(empresas), 200
    else:
        return jsonify({"error": "Região não fornecida"}), 400

@app.route('/atualizar_status_empresa', methods=['POST'])
@jwt_required()
def atualizar_status_empresa_route():
    dados = request.json
    cnpj = dados.get('cnpj')
    novo_status = dados.get('status')
    Empresa.atualizar_status(cnpj, novo_status)
    return jsonify({"message": "Status da empresa atualizado com sucesso!"})

@app.route('/atualizar_ultima_venda', methods=['POST'])
@jwt_required()
def atualizar_ultima_venda_route():
    dados = request.json
    cnpj = dados.get('cnpj')
    ultima_venda = dados.get('ultimaVenda')
    Empresa.atualizar_ultima_venda(cnpj, ultima_venda)
    return jsonify({"message": "Última venda da empresa atualizada com sucesso!"})

@app.route('/atualizar_ultima_visita', methods=['POST'])
@jwt_required()
def atualizar_ultima_visita_route():
    dados = request.json
    cnpj = dados.get('cnpj')
    ultima_visita = dados.get('ultimaVisita')
    Empresa.atualizar_ultima_visita(cnpj, ultima_visita)
    return jsonify({"message": "Última visita da empresa atualizada com sucesso!"})

@app.route('/listar_todos_contatos', methods=['GET'])
@jwt_required()
def listar_todos_contatos_route():
    contatos = Contato.listar_todos()
    return jsonify(contatos)

@app.route('/listar_contato_por_cnpj', methods=['GET'])
@jwt_required()
def listar_contato_por_cnpj_route():
    cnpj = request.args.get('cnpj')
    contatos = Contato.buscar_por_cnpj(cnpj)
    return jsonify(contatos)

@app.route('/deletar_contato', methods=['DELETE'])
@jwt_required()
def deletar_contato():
    data = request.json
    nome = data.get('nome')
    celular = data.get('celular')
    
    if not nome or not celular:
        return jsonify({"error": "Nome e número são necessários"}), 400

    contatos = database.get_database().contatos
    result = contatos.delete_one({"nome": nome, "celular": celular})

    if result.deleted_count == 1:
        return jsonify({"message": "Contato deletado com sucesso"}), 200
    else:
        return jsonify({"error": "Contato não encontrado"}), 404

@app.route('/cadastrar_contato', methods=['POST'])
@jwt_required()
def cadastrar_contato_route():
    valores = request.json
    contato = Contato(**valores)
    contato.inserir_contato()
    return jsonify(contato.formatar_dados())

@app.route('/listar_todas_propostas', methods=['GET'])
@jwt_required()
def listar_todas_propostas_route():
    propostas = Proposta.listar_todas()
    return jsonify(propostas)

@app.route('/listar_proposta_por_cnpj', methods=['GET'])
@jwt_required()
def listar_proposta_por_cnpj_route():
    cnpj = request.args.get('cnpj')
    propostas = Proposta.buscar_por_cnpj(cnpj)
    return jsonify(propostas)

@app.route('/proposta/<int:chave>', methods=['GET'])
@jwt_required()
def listar_proposta_por_id(chave):
    proposta = database.get_database().propostas.find_one({"chave": chave})
    if proposta:
        return jsonify(Proposta(**proposta).formatar_dados())
    else:
        return jsonify({"error": "Proposta não encontrada"}), 404

@app.route('/registrar_proposta', methods=['POST'])
@jwt_required()
def registrar_proposta_route():
    dados = request.json
    proposta = Proposta(**dados)
    proposta.salvar()
    nova_chave = proposta.chave
    return jsonify({"message": "Proposta registrada com sucesso!", "chave": nova_chave})

@app.route('/listar_visitas_por_cnpj', methods=['GET'])
@jwt_required()
def listar_visitas_por_cnpj_route():
    cnpj = request.args.get('cnpj') 
    visitas = Visita.buscar_por_cnpj(cnpj)
    return jsonify(visitas)

@app.route('/cadastrar_visita', methods=['POST'])
@jwt_required()
def cadastrar_visita_route():
    valores = request.json
    visita = Visita(**valores)
    visita.inserir_visita()
    return jsonify(visita.formatar_dados())

@app.route('/upload_imagem/<int:chave>', methods=['POST'])
@jwt_required()
def upload_imagem(chave):
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        propostas = database.get_database().propostas
        propostas.update_one(
            {'chave': chave},
            {'$push': {'imagens': {'descricao': request.form['descricao'], 'path': filename}}}
        )
        return jsonify({'message': 'Imagem uploaded successfully'}), 200

@app.route('/get_imagem/<filename>', methods=['GET'])
@jwt_required()
def get_imagem(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/adicionar_revisao/<int:chave>', methods=['POST'])
@jwt_required()
def adicionar_revisao(chave):
    dados = request.json
    revisao = Revisao(**dados)
    propostas = database.get_database().propostas
    propostas.update_one(
        {'chave': chave},
        {'$push': {'revisoes': revisao.formatar_dados()}}
    )
    return jsonify({'message': 'Revisão adicionada com sucesso!'}), 200

@app.route('/adicionar_tratativa/<int:chave>', methods=['POST'])
@jwt_required()
def adicionar_tratativa(chave):
    dados = request.json
    tratativa = Tratativa(**dados)
    propostas = database.get_database().propostas
    propostas.update_one(
        {'chave': chave},
        {'$push': {'tratativas': tratativa.formatar_dados()}}
    )
    return jsonify({'message': 'Tratativa adicionada com sucesso!'}), 200


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=3000)
    threading.Thread(target=ping_service).start()