from src.models.interfaces.comentario_repository import ComentarioRepositoryInterface
from .interfaces.comentario_inserir_controller import ComentarioInserirControllerInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from src.models.entities.imovel import Comentario

class ComentarioInserirController(ComentarioInserirControllerInterface):
    def __init__(self, comentario_repository: ComentarioRepositoryInterface) -> None:
        self._comentario_repository = comentario_repository

    async def inserir(self, comentario_data: dict) -> dict:
        self._validate_comentario_data(comentario_data)
        comentario = await self.__inserir_comentario(comentario_data)
        return self.__format__response(comentario)
    

    def _validate_comentario_data(self, comentario_data: dict) -> None:
        if not comentario_data.get("texto"):
            raise HttpBadRequestError("Texto do comentário é obrigatório.")
        
    
    async def __inserir_comentario(self, comentario_data: dict) -> Comentario:
        comentario = await self._comentario_repository.inserir_comentario(comentario_data)
        return comentario


    def __format__response(self, comentario: Comentario) -> dict:
        formatted_comentario = { "id": comentario.id, "texto": comentario.texto, "aprovado": comentario.aprovado, "imovel_id": comentario.imovel_id }
        return {
            "type": "Comentário",
            "count": 1,
            "attributes": formatted_comentario
        }