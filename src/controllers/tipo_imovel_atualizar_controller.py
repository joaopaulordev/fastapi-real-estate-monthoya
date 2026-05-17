from src.models.interfaces.tipo_imovel_repository import TipoImovelRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from .interfaces.tipo_imovel_atualizar_controller import TipoImovelAtualizarControllerInterface
from src.models.entities.imovel import TipoImovel

class TipoImovelAtualizarController(TipoImovelAtualizarControllerInterface):
    def __init__(self, tipo_imovel_repository: TipoImovelRepositoryInterface) -> None:
        self._tipo_imovel_repository = tipo_imovel_repository

    async def atualizar(self, tipo_imovel_data: dict) -> dict:    
        self._validate_tipo_imovel_data(tipo_imovel_data)
        tipo_imovel = await self.__atualizar_tipo_imovel(tipo_imovel_data)
        return self.__format__response(tipo_imovel)

    def _validate_tipo_imovel_data(self, tipo_imovel_data: dict) -> None:
        descricao = tipo_imovel_data["descricao"]
        if not descricao:
            raise HttpBadRequestError("Descrição do tipo de imóvel é obrigatório.")        
        

    async def __atualizar_tipo_imovel(self, tipo_imovel_data: dict) -> TipoImovel:
        return await self._tipo_imovel_repository.atualizar_tipo_imovel(tipo_imovel_data)

    def __format__response(self, tipo_imovel: TipoImovel) -> dict:
        formatted_tipo_imovel = { "id": tipo_imovel.id, "descricao": tipo_imovel.descricao }
        return {
            "type": "TipoImovel",
            "count": 1,
            "attributes": formatted_tipo_imovel
        }