from datetime import datetime, timedelta
import random
from database import database
from models import Empresa, Contato, Visita, Proposta

# Gerar dados fictícios
nomes_empresas = [f"Empresa {i}" for i in range(1, 51)]
cnpjs = [f"{random.randint(10000000000000, 99999999999999)}" for _ in range(50)]
regioes = ["71", "73", "74", "75", "77", "79"]  # DDDs da Bahia e Sergipe
municipios = ["Salvador", "Feira de Santana", "Vitória da Conquista", "Camaçari", "Juazeiro"]
ceps = [f"{random.randint(10000, 99999)}-{random.randint(100, 999)}" for _ in range(50)]

funcoes = ["Gerente", "Analista", "Supervisor", "Diretor", "Coordenador"]
nomes_contatos = [f"Contato {i}" for i in range(1, 101)]
emails = [f"contato{i}@empresa.com" for i in range(1, 101)]
telefones = [f"{random.choice(regioes)}{random.randint(10000000, 99999999)}" for _ in range(100)]
celulares = [f"{random.choice(regioes)}{random.randint(900000000, 999999999)}" for _ in range(100)]

# Criar empresas
for i in range(50):
    empresa = Empresa(
        nome_empresa=nomes_empresas[i],
        cnpj=cnpjs[i],
        regiao=random.choice(regioes),
        razao_social=f"Razão Social {i}",
        municipio=random.choice(municipios),
        cep=ceps[i]
    )
    empresa.inserir_empresa()

    # Criar contatos para a empresa
    for _ in range(2):
        contato = Contato(
            cnpj_empresa=empresa.cnpj,
            nome=random.choice(nomes_contatos),
            numero=random.choice(telefones),
            funcao=random.choice(funcoes),
            celular=random.choice(celulares),
            email=random.choice(emails)
        )
        contato.inserir_contato()

    # Criar visitas para a empresa
    for _ in range(2):
        visita = Visita(
            cnpj_empresa=empresa.cnpj,
            data=(datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
            descricao=f"Descrição da visita {random.randint(1, 100)}",
            tipo=random.choice(["Visita Técnica", "Visita Comercial"])
        )
        visita.inserir_visita()

    # Criar propostas para a empresa
    for _ in range(2):
        proposta = Proposta(
            cnpj_empresa=empresa.cnpj,
            referencia=f"REF-{random.randint(1000, 9999)}",
            data=(datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
            observacao=f"Observação da proposta {random.randint(1, 100)}",
            status=random.choice(["Aberta", "Fechada", "Pendente"]),
            descricao=f"Descrição da proposta {random.randint(1, 100)}"
        )
        proposta.salvar()

print("Banco de dados populado com sucesso!")
