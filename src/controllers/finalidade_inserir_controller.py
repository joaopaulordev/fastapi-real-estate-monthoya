from src.models.interfaces.finalidade_repository import FinalidadeRepositoryInterface
from .interfaces.finalidade_inserir_controller import FinalidadeInserirControllerInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from src.models.entities.imovel import Finalidade

class FinalidadeInserirController(FinalidadeInserirControllerInterface):
    def __init__(self, finalidade_repository: FinalidadeRepositoryInterface) -> None:
        self._finalidade_repository = finalidade_repository

    async def inserir(self, finalidade_data: dict) -> dict:    
        self._validate_finalidade_data(finalidade_data)
        finalidade = await self.__inserir_finalidade(finalidade_data)
        return self.__format__response(finalidade)
    

    def _validate_finalidade_data(self, finalidade_data: dict) -> None:
        if not finalidade_data.get("descricao"):
            raise HttpBadRequestError("Descrição da finalidade é obrigatória.")
        
    
    async def __inserir_finalidade(self, finalidade_data: dict) -> Finalidade:
        finalidade = await self._finalidade_repository.inserir_finalidade(finalidade_data)
        return finalidade


    def __format__response(self, finalidade: Finalidade) -> dict:
        formatted_finalidade = { "id": finalidade.id, "descricao": finalidade.descricao }
        return {
            "type": "Finalidade",
            "count": 1,
            "attributes": formatted_finalidade
        }