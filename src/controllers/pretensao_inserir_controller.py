from src.models.interfaces.pretensao_repository import PretensaoRepositoryInterface
from .interfaces.pretensao_inserir_controller import PretensaoInserirControllerInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from src.models.entities.imovel import Pretensao

class PretensaoInserirController(PretensaoInserirControllerInterface):
    def __init__(self, pretensao_repository: PretensaoRepositoryInterface) -> None:
        self._pretensao_repository = pretensao_repository

    async def inserir(self, pretensao_data: dict) -> dict:    
        self._validate_pretensao_data(pretensao_data)
        pretensao = await self.__inserir_pretensao(pretensao_data)
        return self.__format__response(pretensao)
    

    def _validate_pretensao_data(self, pretensao_data: dict) -> None:
        if not pretensao_data.get("descricao"):
            raise HttpBadRequestError("Descrição da pretensão é obrigatória.")
        
    
    async def __inserir_pretensao(self, pretensao_data: dict) -> Pretensao:
        pretensao = await self._pretensao_repository.inserir_pretensao(pretensao_data)
        return pretensao


    def __format__response(self, pretensao: Pretensao) -> dict:
        formatted_pretensao = { "id": pretensao.id, "descricao": pretensao.descricao }
        return {
            "type": "Pretensao",
            "count": 1,
            "attributes": formatted_pretensao
        }