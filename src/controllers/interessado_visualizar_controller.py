from src.models.interfaces.interessado_repository import InteressadoRepositoryInterface
from src.models.entities.imovel import Interessado
from .interfaces.interessado_visualizar_controller import InteressadoVisualizarControllerInterface

class InteressadoVisualizarController(InteressadoVisualizarControllerInterface):
    def __init__(self, interessado_repository: InteressadoRepositoryInterface) -> None:
        self.__interessado_repository = interessado_repository

    async def visualizar(self, interessado_id: int) -> dict:
        interessado = await self.__busca_interessado_db(interessado_id)
        response = self.__format_response(interessado)
        return response

    async def __busca_interessado_db(self, interessado_id: int) -> Interessado:
        interessado = await self.__interessado_repository.visualizar_interessado(interessado_id)
        return interessado

    def __format_response(self, interessado: Interessado) -> dict:
        formatted_interessado = { "id": interessado.id, "nome": interessado.nome, "email": interessado.email, "telefone": interessado.telefone, "estado": interessado.estado, "cidade": interessado.cidade, "imovel_id": interessado.imovel_id }
        return {
            "data": {
                "type": "Interessado",
                "count": 1,
                "attributes": formatted_interessado
            }
        }