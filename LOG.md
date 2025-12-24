# TaskForge — Learning Log

Diário de aprendizado do projeto **TaskForge**, criado para registrar decisões técnicas, progresso e aprendizados durante a prática de Python, Flask e Docker.

---

## 🟢 NÍVEL BÁSICO

### Passo B1 — Base do Projeto

**Objetivo**  
Criar a estrutura inicial do projeto e preparar o ambiente de desenvolvimento local.

**O que foi feito**
- Criada a estrutura inicial de pastas (`frontend`, `backend`, `docs`)
- Repositório Git inicializado desde o primeiro passo
- Ambientes virtuais (`venv`) configurados separadamente para frontend e backend
- Flask instalado em cada aplicação
- Arquivos `requirements.txt` gerados para controle de dependências

**O que aprendi**
- A importância de isolar dependências com ambientes virtuais
- Por que frontend e backend devem ser separados mesmo em projetos pequenos
- Boas práticas iniciais de versionamento e organização de projeto

---

### Passo B2 — Backend Flask Inicial

**Objetivo**  
Criar a primeira aplicação Flask e validar o funcionamento do backend localmente.

**O que foi feito**
- Criado o arquivo principal do backend (`backend/app.py`)
- Inicializada uma aplicação Flask básica
- Criado o endpoint `/health` para verificação do serviço
- Backend executado localmente com o ambiente virtual ativado

**O que aprendi**
- O backend funciona como um servidor HTTP que responde dados em JSON
- Como o Flask utiliza rotas para mapear URLs para funções Python
- A importância de rodar a aplicação dentro do ambiente virtual, mesmo quando ela aparenta funcionar fora dele

📌 **Observação**  
Neste nível, o projeto utiliza dados mockados em memória. A persistência em banco de dados será introduzida apenas em níveis posteriores.


---

### Passo B3 — Arquitetura em camadas e dados mockados

**Objetivo**  
Criar a estrutura básica do backend utilizando separação em camadas e dados mockados.

**O que foi feito**
- Criadas as pastas `routes`, `services` e `repositories`
- Implementado repositório mockado em memória para projetos
- Criado serviço responsável pela regra de negócio
- Criada rota `/projects` utilizando Blueprint
- Registradas as rotas no `app.py`

**O que aprendi**
- Como separar responsabilidades no backend
- Por que não colocar lógica diretamente nas rotas
- Como simular um banco de dados usando dados em memória

**Desafio**
No desafio de buscar projeto por ID, tive dificuldades inicialmente com:
- Diferença entre índice de lista e ID do objeto
- Como receber parâmetros pela URL no Flask

Após a correção, entendi melhor o fluxo:
rota → service → repository → resposta HTTP.


---

### Passo B4 — Tarefas mockadas por projeto

**Objetivo**  
Criar tarefas mockadas e relacioná-las a projetos existentes.

**O que foi feito**
- Criado repositório de tarefas com dados em memória
- Criado serviço de tarefas
- Criada rota para listar tarefas por projeto
- Relacionamento feito via `project_id`

**O que aprendi**
- Como modelar relacionamento entre entidades sem banco de dados
- Como reutilizar o mesmo padrão de arquitetura
- Como pensar domínio antes de pensar banco
