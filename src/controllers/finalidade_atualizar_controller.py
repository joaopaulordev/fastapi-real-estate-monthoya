from src.models.interfaces.finalidade_repository import FinalidadeRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from .interfaces.finalidade_atualizar_controller import FinalidadeAtualizarControllerInterface
from src.models.entities.imovel import Finalidade

class FinalidadeAtualizarController(FinalidadeAtualizarControllerInterface):
    def __init__(self, finalidade_repository: FinalidadeRepositoryInterface) -> None:
        self._finalidade_repository = finalidade_repository

    async def atualizar(self, finalidade_data: dict) -> dict:    
        self._validate_finalidade_data(finalidade_data)
        finalidade = await self.__atualizar_finalidade(finalidade_data)
        return self.__format__response(finalidade)

    def _validate_finalidade_data(self, finalidade_data: dict) -> None:
        descricao = finalidade_data["descricao"]
        if not descricao:
            raise HttpBadRequestError("Descrição da finalidade é obrigatória.")        
        

    async def __atualizar_finalidade(self, finalidade_data: dict) -> Finalidade:
        return await self._finalidade_repository.atualizar_finalidade(finalidade_data)

    def __format__response(self, finalidade: Finalidade) -> dict:
        formatted_finalidade = { "id": finalidade.id, "descricao": finalidade.descricao }
        return {
            "type": "Finalidade",
            "count": 1,
            "finalidade": formatted_finalidade
        }