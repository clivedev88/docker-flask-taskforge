TASKFORGE
-> Descricao:

Um App Web de produtividade com:

Login;
Projetos;
Tarefas por projetos.
-> Stack

É um projeto simples, mas completo com um Stack simples:

Frontend: Python + Flasck + Jinja + Bootstrap
Backend: Python + Flask
Banco de Dados: PostGreSQL
Deploy: DOCKER
-> Arquitetura:

Backend:
routes: para entradas HTTP ou endpoints
services: contém a lógica ou regars de negócio
repositories: dá acesso a dados mockados
schemas: cuidará da valida;ão e DTO.
Frontend:
templates: HTML com Jinja.
static: CSS, JS e imagens