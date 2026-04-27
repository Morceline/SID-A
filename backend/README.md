# Backend (API)

Responsável pelo processamento dos dados e regras de negócio.

Tecnologia prevista:
- Python (FastAPI)
- PostgreSQL

## Etapa 1 
**Execução (Backend - Protótipo Inicial)**

1. Acessar pasta backend
 cd backend

2. Criar ambiente virtual
 python -m venv venv

3. Ativar ambiente
 source venv/Scripts/activate

4. Instalar dependências
 pip install -r requirements.txt

5. Executar servidor
 uvicorn app:app --reload

6. Acessar
 http://127.0.0.1:8000

## Etapa 2
 **Instale:**
 - pip install passlib[bcrypt]  #Segurança (senha)
 - pip install python-jose  #Token JWT
 - pip install pydantic[email]  #Validação

 **Atualize o requirements.txt**
 - pip freeze > requirements.txt