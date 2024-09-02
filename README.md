Sistema de Gerenciamento de Vendas e Propostas de Projetos de Engenharia Mecânica
Este projeto é um sistema completo de gerenciamento de vendas e propostas para projetos de engenharia mecânica. Ele foi desenvolvido com um frontend em React, um backend em Flask, e utiliza MongoDB com Mongoose como ORM para armazenar e gerenciar os dados.

Funcionalidades
1. Gerenciamento de Vendas
Cadastro de Vendas:

Permite o cadastro de vendas de projetos, incluindo informações como nome do cliente, descrição do projeto, valor da venda, e status (em andamento, concluído, cancelado).
Consulta de Vendas:

Listagem de todas as vendas cadastradas, com filtros por status, cliente ou data.
Exibição detalhada das informações de uma venda específica ao selecionar a venda na lista.
Atualização de Vendas:

Permite a edição das informações de uma venda, como atualização do status ou alteração do valor.
Remoção de Vendas:

Permite a exclusão de uma venda específica após confirmação do usuário.
2. Gerenciamento de Propostas
Criação de Propostas:

Permite a criação de propostas de projetos com detalhes como descrição técnica, estimativa de custos, prazos e condições comerciais.
Consulta de Propostas:

Listagem de todas as propostas criadas, com filtros por status (aceito, pendente, rejeitado) ou cliente.
Detalhamento de uma proposta específica com informações completas.
Atualização de Propostas:

Permite a modificação dos detalhes de uma proposta, incluindo revisões técnicas e ajustes de custos.
Remoção de Propostas:

Permite a exclusão de uma proposta específica com confirmação.
3. Integração Frontend e Backend
Interface de Usuário em React:

Interface interativa e responsiva para gerenciar vendas e propostas.
Componentes reutilizáveis para visualização e manipulação dos dados.
API RESTful em Flask:

O backend em Flask fornece uma API RESTful para manipulação de dados, com endpoints para operações de CRUD (Create, Read, Update, Delete) tanto para vendas quanto para propostas.
Banco de Dados MongoDB com Mongoose:

Armazena os dados de vendas e propostas, utilizando o Mongoose como ORM para modelagem dos dados e interação com o MongoDB.
Tecnologias Utilizadas
Frontend:

React
Axios para chamadas HTTP ao backend
React Router para navegação entre páginas
Backend:

Flask com Python
Flask-CORS para lidar com políticas de CORS
Flask-PyMongo para integração com MongoDB
Banco de Dados:

MongoDB para armazenamento de dados
Mongoose para modelagem de dados e integração com MongoDB
Configuração do Ambiente
Pré-requisitos
Node.js (para o frontend)
Python 3.x (para o backend)
MongoDB (local ou em um cluster na nuvem)
Executando o Projeto
Backend (Flask)
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/gerenciamento-vendas-propostas.git
Navegue até o diretório do backend:

bash
Copiar código
cd gerenciamento-vendas-propostas/backend
Crie e ative um ambiente virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Para Linux/MacOS
venv\Scripts\activate  # Para Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configure as variáveis de ambiente:

Crie um arquivo .env com as configurações necessárias (ex.: URI do MongoDB).
Inicie o servidor Flask:

bash
Copiar código
flask run
Frontend (React)
Navegue até o diretório do frontend:

bash
Copiar código
cd gerenciamento-vendas-propostas/frontend
Instale as dependências:

bash
Copiar código
npm install
Inicie o servidor de desenvolvimento:

bash
Copiar código
npm start
Acesse o sistema:

O frontend estará disponível em http://localhost:3000.
Estrutura do Projeto
/backend: Contém todo o código do servidor Flask, incluindo rotas, modelos de dados e lógica de negócio.
/frontend: Contém o código React, incluindo componentes, páginas e estilos.
/backend/models: Modelos de dados definidos com Mongoose.
/frontend/src: Código fonte do React, organizado em componentes e páginas.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou correções.
