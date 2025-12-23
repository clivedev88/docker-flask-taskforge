# TaskForge — Diário de Aprendizado

Projeto didático para praticar **Python**, **Flask** e **Docker** do zero.

---

## PASSO 1 — Base do Projeto

### Objetivo
Criar a estrutura inicial do projeto e preparar o ambiente de desenvolvimento.

### O que foi feito
- Criada a estrutura de pastas (`frontend`, `backend`, `docs`)
- Git inicializado
- Ambientes virtuais (venv) configurados separadamente para frontend e backend
- Flask instalado em cada aplicação
- Arquivos `requirements.txt` criados

### O que aprendi
- A importância de usar ambientes virtuais
- Separação clara entre frontend e backend
- Boas práticas iniciais de versionamento

---

## PASSO 2 — Instalação de Dependências

### Backend
```bash
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

### Frontend
```
cd frontend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

📌 Observação:
Este projeto inicia com dados mockados. O banco de dados será introduzido apenas em níveis posteriores.


---

# 4️⃣ Versionamento correto agora (MUITO IMPORTANTE)

Depois das correções:

```powershell
git add README.md REVIEW.md
git commit -m "docs: improve README and learning review documentation"
