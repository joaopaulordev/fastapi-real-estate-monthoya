from src.errors.types.http_not_found_error import HttpNotFoundError
from src.models.interfaces.comentario_repository import ComentarioRepositoryInterface
from .interfaces.comentario_deletar_controller import ComentarioDeletarControllerInterface
import os

class ComentarioDeletarController(ComentarioDeletarControllerInterface):
    def __init__(self, comentario_repository: ComentarioRepositoryInterface) -> None:
        self.__comentario_repository = comentario_repository

    async def deletar(self, comentario_id: int) -> dict:            
        comentario = await self.__comentario_repository.deletar_comentario(comentario_id)
        return {
            "message": f"Comentário {comentario.id} deletado com sucesso."
        }


