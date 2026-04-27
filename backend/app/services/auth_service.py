from app.models.usuario import Usuario
from app.services.security import hash_senha, verificar_senha
from app.services.token import criar_token

def registrar_usuario(db, dados):
    usuario_existente = db.query(Usuario).filter(Usuario.email == dados.email).first()

    if usuario_existente:
        return None

    novo_usuario = Usuario(
        nome=dados.nome,
        email=dados.email,
        senha=hash_senha(dados.senha)
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


def autenticar_usuario(db, dados):
    user = db.query(Usuario).filter(Usuario.email == dados.email).first()

    if not user:
        return None

    if not verificar_senha(dados.senha, user.senha):
        return None

    token = criar_token({"sub": str(user.id)})

    return {
        "user": user,
        "token": token
    }