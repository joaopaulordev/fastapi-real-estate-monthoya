from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("CORS_URLS")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from src.main.routes.imoveis_routes import imoveis_routes
from src.main.routes.fotos_routes import fotos_routes
from src.main.routes.foto_localizacao_routes import foto_localizacao_routes
from src.main.routes.comentarios_routes import comentario_routes
from src.main.routes.interessados_routes import interessado_routes
from src.main.routes.finalidades_routes import finalidade_routes
from src.main.routes.tipo_imoveis_routes import tipo_imovel_routes
from src.main.routes.pretensoes_routes import pretensao_routes
from src.main.routes.configuracoes_routes import configuracao_routes
from src.main.routes.config_whatsapp_routes import configwhatsapp_routes
from src.main.routes.auth_routes import auth_router

# Mount the 'uploads' folder to the '/uploads' URL path
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(auth_router)
app.include_router(configwhatsapp_routes)
app.include_router(configuracao_routes)
app.include_router(finalidade_routes)
app.include_router(tipo_imovel_routes)
app.include_router(pretensao_routes)
app.include_router(imoveis_routes)
app.include_router(foto_localizacao_routes)
app.include_router(fotos_routes)
app.include_router(comentario_routes)
app.include_router(interessado_routes)
