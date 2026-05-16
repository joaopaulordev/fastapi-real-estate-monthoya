from typing import Dict
from src.models.interfaces.comentario_repository import ComentarioRepositoryInterface
from src.models.entities.imovel import Comentario
from .interfaces.comentario_visualizar_controller import ComentarioVisualizarControllerInterface

class ComentarioVisualizarController(ComentarioVisualizarControllerInterface):
    def __init__(self, comentario_repository: ComentarioRepositoryInterface) -> None:
        self.__comentario_repository = comentario_repository

    async def visualizar(self, comentario_id: int) -> dict:
        comentario = await self.__busca_comentario_db(comentario_id)
        response = self.__format_response(comentario)
        return response

    async def __busca_comentario_db(self, comentario_id: int) -> Comentario:
        comentario = await self.__comentario_repository.visualizar_comentario(comentario_id)
        return comentario

    def __format_response(self, comentario: Comentario) -> dict:
        formatted_comentario = { "id": comentario.id, "texto": comentario.texto, "aprovado": comentario.aprovado, "imovel_id": comentario.imovel_id }
        return {
            "data": {
                "type": "Comentário",
                "count": 1,
                "attributes": formatted_comentario
            }
        }