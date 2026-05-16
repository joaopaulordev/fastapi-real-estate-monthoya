from src.models.interfaces.comentario_repository import ComentarioRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from .interfaces.comentario_atualizar_controller import ComentarioAtualizarControllerInterface
from src.models.entities.imovel import Comentario

class ComentarioAtualizarController(ComentarioAtualizarControllerInterface):
    def __init__(self, comentario_repository: ComentarioRepositoryInterface) -> None:
        self._comentario_repository = comentario_repository

    async def atualizar(self, comentario_data: dict) -> dict:
        self._validate_comentario_data(comentario_data)
        comentario = await self.__atualizar_comentario(comentario_data)
        return self.__format__response(comentario)

    def _validate_comentario_data(self, comentario_data: dict) -> None:
        texto = comentario_data["texto"]
        if not texto:
            raise HttpBadRequestError("Texto do comentário é obrigatório.")        
        

    async def __atualizar_comentario(self, comentario_data: dict) -> Comentario:
        return await self._comentario_repository.atualizar_comentario(comentario_data)

    def __format__response(self, comentario: Comentario) -> dict:
        formatted_comentario = { "id": comentario.id, "texto": comentario.texto, "aprovado": comentario.aprovado, "imovel_id": comentario.imovel_id }
        return {
            "type": "Comentário",
            "count": 1,
            "attributes": formatted_comentario
        }