from src.models.interfaces.tipo_imovel_repository import TipoImovelRepositoryInterface
from src.models.entities.imovel import TipoImovel
from .interfaces.tipo_imovel_visualizar_controller import TipoImovelVisualizarControllerInterface

class TipoImovelVisualizarController(TipoImovelVisualizarControllerInterface):
    def __init__(self, tipo_imovel_repository: TipoImovelRepositoryInterface) -> None:
        self.__tipo_imovel_repository = tipo_imovel_repository

    async def visualizar(self, tipo_imovel_id: int) -> dict:        
        tipo_imovel = await self.__busca_tipo_imovel_db(tipo_imovel_id)
        response = self.__format_response(tipo_imovel)
        return response

    async def __busca_tipo_imovel_db(self, tipo_imovel_id: int) -> TipoImovel:
        tipo_imovel = await self.__tipo_imovel_repository.visualizar_tipo_imovel(tipo_imovel_id)
        return tipo_imovel

    def __format_response(self, tipo_imovel: TipoImovel) -> dict:
        formatted_tipo_imovel = { "id": tipo_imovel.id, "descricao": tipo_imovel.descricao }
        return {
            "data": {
                "type": "TipoImovel",
                "count": 1,
                "attributes": formatted_tipo_imovel
            }
        }