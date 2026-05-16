from typing import List
from src.models.interfaces.comentario_repository import ComentarioRepositoryInterface
from src.models.entities.imovel import Comentario
from .interfaces.comentario_listar_controller import ComentarioListarControllerInterface

class ComentarioListarController(ComentarioListarControllerInterface):
    def __init__(self, comentario_repository: ComentarioRepositoryInterface) -> None:
        self.__comentario_repository = comentario_repository

    async def listar(self, imovel_id: int) -> dict:
        comentarios = await self.__buscar_comentarios_db(imovel_id)
        response = self.__format_response(comentarios)
        return response

    async def __buscar_comentarios_db(self, imovel_id: int) -> List[Comentario]:
        comentarios = await self.__comentario_repository.listar_comentarios(imovel_id)
        return comentarios

    def __format_response(self, comentarios: List[Comentario]) -> dict:
        formatted_comentarios = [{ "id": comentario.id, "texto": comentario.texto, "aprovado": comentario.aprovado, "imovel_id": comentario.imovel_id } for comentario in comentarios]
        return {
            "data": {
                "type": "Comentarios",
                "count": len(formatted_comentarios),
                "attributes": formatted_comentarios
            }
        }
