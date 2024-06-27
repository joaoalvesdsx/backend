from datetime import datetime
from database import database
from bson import ObjectId, errors


def get_next_id(collection_name):
    counters = database.get_database().counters
    counter = counters.find_one_and_update(
        {"_id": collection_name},
        {"$inc": {"seq": 1}},
        return_document=True,
        upsert=True
    )
    return counter["seq"]

class Empresa:
    def __init__(self, nome_empresa, cnpj, regiao, razao_social, municipio, cep, status='Ativo', ultimaVenda=None, ultimaVisita=None, chave=None, **kwargs):
        self.chave = chave if chave is not None else get_next_id('empresas')
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.regiao = regiao
        self.razao_social = razao_social
        self.municipio = municipio
        self.cep = cep
        self.status = status
        self.ultimaVenda = ultimaVenda
        self.ultimaVisita = ultimaVisita

    def inserir_empresa(self):
        empresas = database.get_database().empresas
        empresas.insert_one(self.formatar_dados())

    @staticmethod
    def buscar_por_cnpj(cnpj):
        empresas = database.get_database().empresas
        empresa_data = empresas.find_one({"cnpj": cnpj})
        return Empresa(**empresa_data).formatar_informacoes() if empresa_data else None

    @staticmethod
    def buscar_por_regiao(regiao):
        empresas = database.get_database().empresas
        return [Empresa(**empresa_data).formatar_dados() for empresa_data in empresas.find({"regiao": regiao})]
    
    @staticmethod
    def listar_todas():
        empresas = database.get_database().empresas
        return [Empresa(**empresa_data).formatar_dados() for empresa_data in empresas.find()]

    @staticmethod
    def atualizar_status(cnpj, novo_status):
        empresas = database.get_database().empresas
        empresas.update_one({"cnpj": cnpj}, {"$set": {"status": novo_status}})

    @staticmethod
    def atualizar_ultima_venda(cnpj, ultima_venda):
        empresas = database.get_database().empresas
        empresas.update_one({"cnpj": cnpj}, {"$set": {"ultimaVenda": ultima_venda}})

    @staticmethod
    def atualizar_ultima_visita(cnpj, ultima_visita):
        empresas = database.get_database().empresas
        empresas.update_one({"cnpj": cnpj}, {"$set": {"ultimaVisita": ultima_visita}})

    def formatar_informacoes(self):
        return {
            "chave": self.chave,
            "nome_empresa": self.nome_empresa,
            "cnpj": self.cnpj,
            "regiao": self.regiao,
            "razao_social": self.razao_social,
            "municipio": self.municipio,
            "cep": self.cep,
            "status": self.status,
            "ultimaVenda": self.ultimaVenda,
            "ultimaVisita": self.ultimaVisita
        }

    def formatar_dados(self):
        return {
            "chave": self.chave,
            "nome_empresa": self.nome_empresa,
            "cnpj": self.cnpj,
            "regiao": self.regiao,
            "razao_social": self.razao_social,
            "municipio": self.municipio,
            "cep": self.cep,
            "status": self.status,
            "ultimaVenda": self.ultimaVenda,
            "ultimaVisita": self.ultimaVisita
        }

class Contato:
    def __init__(self, cnpj_empresa, nome, numero, funcao, celular, email, observacao='', chave=None, **kwargs):
        self.chave = chave if chave is not None else get_next_id('contatos')
        self.cnpj_empresa = cnpj_empresa
        self.nome = nome
        self.numero = numero
        self.funcao = funcao
        self.celular = celular
        self.email = email
        self.observacao = observacao

    def inserir_contato(self):
        contatos = database.get_database().contatos
        contatos.insert_one(self.formatar_dados())

    @staticmethod
    def buscar_por_cnpj(cnpj):
        contatos = database.get_database().contatos
        return [Contato(**contato_data).formatar_dados() for contato_data in contatos.find({"cnpj_empresa": cnpj})]
    
    @staticmethod
    def buscar_por_id(chave):
        contatos = database.get_database().contatos
        contato_data = contatos.find_one({"chave": chave})
        return Contato(**contato_data).formatar_dados() if contato_data else None
    
    @staticmethod
    def listar_todos():
        contatos = database.get_database().contatos
        return [Contato(**contato_data).formatar_dados() for contato_data in contatos.find()]

    @staticmethod
    def deletar_contato(chave):
        contatos = database.get_database().contatos
        contatos.delete_one({"chave": chave})

    def formatar_dados(self):
        return {
            "chave": self.chave,
            "cnpj_empresa": self.cnpj_empresa,
            "nome": self.nome,
            "numero": self.numero,
            "funcao": self.funcao,
            "celular": self.celular,
            "email": self.email,
            "observacao": self.observacao
        }

class Imagem:
    def __init__(self, descricao, path, chave=None, **kwargs):
        self.chave = chave if chave is not None else get_next_id('imagens')
        self.descricao = descricao
        self.path = path

    def formatar_dados(self):
        return {
            "chave": self.chave,
            "descricao": self.descricao,
            "path": self.path
        }

class Revisao:
    def __init__(self, data, revisao, descricao, chave=None, **kwargs):
        self.chave = chave if chave is not None else get_next_id('revisoes')
        self.data = data
        self.revisao = revisao
        self.descricao = descricao

    def formatar_dados(self):
        return {
            "chave": self.chave,
            "data": self.data,
            "revisao": self.revisao,
            "descricao": self.descricao
        }

class Tratativa:
    def __init__(self, data, descricao, chave=None, **kwargs):
        self.chave = chave if chave is not None else get_next_id('tratativas')
        self.data = data
        self.descricao = descricao

    def formatar_dados(self):
        return {
            "chave": self.chave,
            "data": self.data,
            "descricao": self.descricao
        }

class Proposta:
    def __init__(self, cnpj_empresa, referencia, data, observacao, status, descricao, imagens=None, revisoes=None, tratativas=None, chave=None, **kwargs):
        self.chave = chave if chave is not None else get_next_id('propostas')
        self.cnpj_empresa = cnpj_empresa
        self.referencia = referencia
        self.data = data
        self.observacao = observacao
        self.status = status
        self.descricao = descricao
        self.imagens = [Imagem(**img) for img in imagens] if imagens else []
        self.revisoes = [Revisao(**rev) for rev in revisoes] if revisoes else []
        self.tratativas = [Tratativa(**trat) for trat in tratativas] if tratativas else []

    def salvar(self):
        propostas = database.get_database().propostas
        propostas.insert_one(self.formatar_dados())

    
    
    @staticmethod
    def buscar_por_cnpj(cnpj):
        propostas = database.get_database().propostas
        return [Proposta(**proposta_data).formatar_dados() for proposta_data in propostas.find({"cnpj_empresa": cnpj})]

    @staticmethod
    def listar_todas():
        propostas = database.get_database().propostas
        return [Proposta(**proposta_data).formatar_dados() for proposta_data in propostas.find()]

    def formatar_dados(self):
        return {
            "chave": self.chave,
            "cnpj_empresa": self.cnpj_empresa,
            "referencia": self.referencia,
            "data": self.data,
            "observacao": self.observacao,
            "status": self.status,
            "descricao": self.descricao,
            "imagens": [img.formatar_dados() for img in self.imagens],
            "revisoes": [rev.formatar_dados() for rev in self.revisoes],
            "tratativas": [trat.formatar_dados() for trat in self.tratativas]
        }

class Visita:
    def __init__(self, cnpj_empresa, data, descricao, tipo, chave=None, **kwargs):
        self.chave = chave if chave is not None else get_next_id('visitas')
        self.cnpj_empresa = cnpj_empresa
        self.data = data
        self.descricao = descricao
        self.tipo = tipo

    def inserir_visita(self):
        visitas = database.get_database().visitas
        visitas.insert_one(self.formatar_dados())

    @staticmethod
    def buscar_por_cnpj(cnpj):
        visitas = database.get_database().visitas
        return [Visita(**visita_data).formatar_dados() for visita_data in visitas.find({"cnpj_empresa": cnpj})]

    @staticmethod
    def listar_todas():
        visitas = database.get_database().visitas
        return [Visita(**visita_data).formatar_dados() for visita_data in visitas.find()]

    def formatar_dados(self):
        return {
            "chave": self.chave,
            "cnpj_empresa": self.cnpj_empresa,
            "data": self.data,
            "descricao": self.descricao,
            "tipo": self.tipo
        }
