from typing import List
from src.models.interfaces.pretensao_repository import PretensaoRepositoryInterface
from src.models.entities.imovel import Pretensao
from .interfaces.pretensao_listar_controller import PretensaoListarControllerInterface

class PretensaoListarController(PretensaoListarControllerInterface):
    def __init__(self, pretensao_repository: PretensaoRepositoryInterface) -> None:
        self.__pretensao_repository = pretensao_repository

    async def listar(self) -> dict:    
        pretensaos = await self.__buscar_pretensaos_db()
        response = self.__format_response(pretensaos)
        return response

    async def __buscar_pretensaos_db(self) -> List[Pretensao]:
        pretensaos = await self.__pretensao_repository.listar_pretensoes()
        return pretensaos

    def __format_response(self, pretensaos: List[Pretensao]) -> dict:
        formatted_pretensaos = [{ "id": pretensao.id, "descricao": pretensao.descricao} for pretensao in pretensaos]
        return {
            "data": {
                "type": "Pretensao",
                "count": len(formatted_pretensaos),
                "attributes": formatted_pretensaos
            }
        }
