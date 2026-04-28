from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.usuario import UsuarioCreate, UsuarioLogin
from app.services.auth_service import registrar_usuario, autenticar_usuario

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(dados: UsuarioCreate, db: Session = Depends(get_db)):
    user = registrar_usuario(db, dados)

    if not user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    return {"msg": "Usuário criado com sucesso"}

@router.post("/login")
def login(dados: UsuarioLogin, db: Session = Depends(get_db)):
    resultado = autenticar_usuario(db, dados)

    if not resultado:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    return {
        "token": resultado["token"],
        "nome": resultado["user"].nome
    }