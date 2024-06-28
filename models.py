from datetime import datetime
from database import database, get_next_sequence_value, decrement_sequence_value

class Empresa:
    def __init__(self, nome_empresa, cnpj, regiao, razao_social, municipio, cep, status='Ativo', ultimaVenda=None, ultimaVisita=None, id=None, **kwargs):
        self._id = id if id else get_next_sequence_value('empresa_id')
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
        empresas = database.empresas
        empresas.insert_one(self.formatar_dados())

    @staticmethod
    def cnpj_existe(cnpj):
        empresas = database.empresas
        return empresas.find_one({'cnpj': cnpj}) is not None

    @staticmethod
    def buscar_por_cnpj(cnpj):
        empresas = database.empresas
        empresa_data = empresas.find_one({"cnpj": cnpj})
        return Empresa(**empresa_data).formatar_informacoes() if empresa_data else None

    @staticmethod
    def buscar_por_regiao(regiao):
        empresas = database.empresas
        return [Empresa(**empresa_data).formatar_dados() for empresa_data in empresas.find({"regiao": regiao})]

    @staticmethod
    def listar_todas():
        empresas = database.empresas
        return [Empresa(**empresa_data).formatar_dados() for empresa_data in empresas.find()]

    @staticmethod
    def atualizar_status(cnpj, novo_status):
        empresas = database.empresas
        empresas.update_one({"cnpj": cnpj}, {"$set": {"status": novo_status}})

    @staticmethod
    def atualizar_ultima_venda(cnpj, ultima_venda):
        empresas = database.empresas
        empresas.update_one({"cnpj": cnpj}, {"$set": {"ultimaVenda": ultima_venda}})

    @staticmethod
    def atualizar_ultima_visita(cnpj, ultima_visita):
        empresas = database.empresas
        empresas.update_one({"cnpj": cnpj}, {"$set": {"ultimaVisita": ultima_visita}})

    @staticmethod
    def deletar_empresa(cnpj):
        empresas = database.empresas
        empresa = empresas.find_one({"cnpj": cnpj})
        if empresa:
            result = empresas.delete_one({"cnpj": cnpj})
            if result.deleted_count > 0:
                decrement_sequence_value('empresa_id')
                return True
        return False

    def formatar_informacoes(self):
        return {
            "_id": self._id,
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
            "_id": self._id,
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
    def __init__(self, cnpj_empresa, nome, telefone, funcao, celular, email, observacao='', id=None, **kwargs):
        self._id = id if id else get_next_sequence_value('contato_id')
        self.cnpj_empresa = cnpj_empresa
        self.nome = nome
        self.telefone = telefone
        self.funcao = funcao
        self.celular = celular
        self.email = email
        self.observacao = observacao

    def inserir_contato(self):
        contatos = database.contatos
        contatos.insert_one(self.formatar_dados())

    @staticmethod
    def buscar_por_cnpj(cnpj):
        contatos = database.contatos
        return [Contato(**contato_data).formatar_dados() for contato_data in contatos.find({"cnpj_empresa": cnpj})]

    @staticmethod
    def buscar_por_id(_id):
        contatos = database.contatos
        contato_data = contatos.find_one({"_id": _id})
        return Contato(**contato_data).formatar_dados() if contato_data else None

    @staticmethod
    def listar_todos():
        contatos = database.contatos
        return [Contato(**contato_data).formatar_dados() for contato_data in contatos.find()]

    @staticmethod
    def atualizar_contato(_id, update_fields):
        contatos = database.contatos
        result = contatos.update_one({"_id": _id}, {"$set": update_fields})
        return result.modified_count > 0

    @staticmethod
    def deletar_contato(_id):
        contatos = database.contatos
        contato = contatos.find_one({"_id": _id})
        if contato:
            result = contatos.delete_one({"_id": _id})
            if result.deleted_count > 0:
                decrement_sequence_value('contato_id')
                return True
        return False

    def formatar_dados(self):
        return {
            "_id": self._id,
            "cnpj_empresa": self.cnpj_empresa,
            "nome": self.nome,
            "telefone": self.telefone,
            "funcao": self.funcao,
            "celular": self.celular,
            "email": self.email,
            "observacao": self.observacao
        }

class Imagem:
    def __init__(self, descricao, path, id=None, **kwargs):
        self._id = id if id else get_next_sequence_value('imagem_id')
        self.descricao = descricao
        self.path = path

    def formatar_dados(self):
        return {
            "_id": self._id,
            "descricao": self.descricao,
            "path": self.path
        }

class Revisao:
    def __init__(self, data, revisao, descricao, id=None, **kwargs):
        self._id = id if id else get_next_sequence_value('revisao_id')
        self.data = data
        self.revisao = revisao
        self.descricao = descricao

    def formatar_dados(self):
        return {
            "_id": self._id,
            "data": self.data,
            "revisao": self.revisao,
            "descricao": self.descricao
        }

class Tratativa:
    def __init__(self, data, descricao, id=None, **kwargs):
        self._id = id if id else get_next_sequence_value('tratativa_id')
        self.data = data
        self.descricao = descricao

    def formatar_dados(self):
        return {
            "_id": self._id,
            "data": self.data,
            "descricao": self.descricao
        }

class Proposta:
    def __init__(self, cnpj_empresa, referencia, data, observacao, status, descricao, imagens=None, revisoes=None, tratativas=None, id=None, **kwargs):
        self._id = id if id else get_next_sequence_value('proposta_id')
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
        propostas = database.propostas
        propostas.insert_one(self.formatar_dados())

    @staticmethod
    def buscar_por_cnpj(cnpj):
        propostas = database.propostas
        return [Proposta(**proposta_data).formatar_dados() for proposta_data in propostas.find({"cnpj_empresa": cnpj})]

    @staticmethod
    def listar_todas():
        propostas = database.propostas
        return [Proposta(**proposta_data).formatar_dados() for proposta_data in propostas.find()]

    @staticmethod
    def atualizar_proposta(_id, update_fields):
        propostas = database.propostas
        result = propostas.update_one({"_id": _id}, {"$set": update_fields})
        return result.modified_count > 0

    @staticmethod
    def deletar_proposta(_id):
        propostas = database.propostas
        proposta = propostas.find_one({"_id": _id})
        if proposta:
            result = propostas.delete_one({"_id": _id})
            if result.deleted_count > 0:
                decrement_sequence_value('proposta_id')
                return True
        return False

    def formatar_dados(self):
        return {
            "_id": self._id,
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
    def __init__(self, cnpj_empresa, data, descricao, tipo, id=None, **kwargs):
        self._id = id if id else get_next_sequence_value('visita_id')
        self.cnpj_empresa = cnpj_empresa
        self.data = data
        self.descricao = descricao
        self.tipo = tipo

    def inserir_visita(self):
        visitas = database.visitas
        visitas.insert_one(self.formatar_dados())

    @staticmethod
    def buscar_por_cnpj(cnpj):
        visitas = database.visitas
        return [Visita(**visita_data).formatar_dados() for visita_data in visitas.find({"cnpj_empresa": cnpj})]

    @staticmethod
    def listar_todas():
        visitas = database.visitas
        return [Visita(**visita_data).formatar_dados() for visita_data in visitas.find()]

    def formatar_dados(self):
        return {
            "_id": self._id,
            "cnpj_empresa": self.cnpj_empresa,
            "data": self.data,
            "descricao": self.descricao,
            "tipo": self.tipo
        }
