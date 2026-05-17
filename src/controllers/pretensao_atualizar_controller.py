from src.models.interfaces.pretensao_repository import PretensaoRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from .interfaces.pretensao_atualizar_controller import PretensaoAtualizarControllerInterface
from src.models.entities.imovel import Pretensao

class PretensaoAtualizarController(PretensaoAtualizarControllerInterface):
    def __init__(self, pretensao_repository: PretensaoRepositoryInterface) -> None:
        self._pretensao_repository = pretensao_repository

    async def atualizar(self, pretensao_data: dict) -> dict:    
        self._validate_pretensao_data(pretensao_data)
        pretensao = await self.__atualizar_pretensao(pretensao_data)
        return self.__format__response(pretensao)

    def _validate_pretensao_data(self, pretensao_data: dict) -> None:
        descricao = pretensao_data["descricao"]
        if not descricao:
            raise HttpBadRequestError("Descrição da pretensão é obrigatória.")        
        

    async def __atualizar_pretensao(self, pretensao_data: dict) -> Pretensao:
        return await self._pretensao_repository.atualizar_pretensao(pretensao_data)

    def __format__response(self, pretensao: Pretensao) -> dict:
        formatted_pretensao = { "id": pretensao.id, "descricao": pretensao.descricao }
        return {
            "type": "Pretensao",
            "count": 1,
            "attributes": formatted_pretensao
        }