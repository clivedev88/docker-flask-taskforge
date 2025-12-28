# 1. imagem base
FROM python:3.12-slim

# 2. diretório de trabalho dentro do container
WORKDIR /app

# 3. copiar dependências primeiro (isto é uma boa prática de cache)
COPY requirements.txt .

# 4. instalar dependências
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

# 5. Copiar o resto do código
COPY . .

# 6. expor a porta da API
EXPOSE 5000

# 7. rodar a aplica;ão
CMD [ "python", "app.py" ]
