from fastapi import FastAPI
from src.main.routes.imoveis_routes import imoveis_routes
from src.main.routes.fotos_routes import fotos_routes
from src.main.routes.comentarios_routes import comentario_routes

app = FastAPI()

app.include_router(imoveis_routes)
app.include_router(fotos_routes)
app.include_router(comentario_routes)
