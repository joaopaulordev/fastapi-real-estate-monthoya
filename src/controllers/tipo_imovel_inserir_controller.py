from src.models.interfaces.tipo_imovel_repository import TipoImovelRepositoryInterface
from .interfaces.tipo_imovel_inserir_controller import TipoImovelInserirControllerInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from src.models.entities.imovel import TipoImovel

class TipoImovelInserirController(TipoImovelInserirControllerInterface):
    def __init__(self, tipo_imovel_repository: TipoImovelRepositoryInterface) -> None:
        self._tipo_imovel_repository = tipo_imovel_repository

    async def inserir(self, tipo_imovel_data: dict) -> dict:  
        self._validate_tipo_imovel_data(tipo_imovel_data)
        tipo_imovel = await self.__inserir_tipo_imovel(tipo_imovel_data)
        return self.__format__response(tipo_imovel)
    

    def _validate_tipo_imovel_data(self, tipo_imovel_data: dict) -> None:
        if not tipo_imovel_data.get("descricao"):
            raise HttpBadRequestError("Descrição do tipo de imóvel é obrigatória.")
        
    
    async def __inserir_tipo_imovel(self, tipo_imovel_data: dict) -> TipoImovel:
        tipo_imovel = await self._tipo_imovel_repository.inserir_tipo_imovel(tipo_imovel_data)
        return tipo_imovel


    def __format__response(self, tipo_imovel: TipoImovel) -> dict:
        formatted_tipo_imovel = { "id": tipo_imovel.id, "descricao": tipo_imovel.descricao }
        return {
            "type": "TipoImovel",
            "count": 1,
            "attributes": formatted_tipo_imovel
        }