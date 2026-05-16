from typing import List
from src.models.interfaces.interessado_repository import InteressadoRepositoryInterface
from src.models.entities.imovel import Interessado
from .interfaces.interessado_listar_controller import InteressadoListarControllerInterface

class InteressadoListarController(InteressadoListarControllerInterface):
    def __init__(self, interessado_repository: InteressadoRepositoryInterface) -> None:
        self.__interessado_repository = interessado_repository

    async def listar(self, imovel_id: int) -> dict:    
        interessados = await self.__buscar_interessados_db(imovel_id)
        response = self.__format_response(interessados)
        return response

    async def __buscar_interessados_db(self, imovel_id: int) -> List[Interessado]:
        interessados = await self.__interessado_repository.listar_interessados(imovel_id)
        return interessados

    def __format_response(self, interessados: List[Interessado]) -> dict:
        formatted_interessados = [{ "id": interessado.id, "nome": interessado.nome, "email": interessado.email, "telefone": interessado.telefone, "estado": interessado.estado, "cidade": interessado.cidade, "imovel_id": interessado.imovel_id } for interessado in interessados]
        return {
            "data": {
                "type": "Interessados",
                "count": len(formatted_interessados),
                "attributes": formatted_interessados
            }
        }
