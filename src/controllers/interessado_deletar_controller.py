from src.models.interfaces.interessado_repository import InteressadoRepositoryInterface
from .interfaces.interessado_deletar_controller import InteressadoDeletarControllerInterface
import os

class InteressadoDeletarController(InteressadoDeletarControllerInterface):
    def __init__(self, interessado_repository: InteressadoRepositoryInterface) -> None:
        self.__interessado_repository = interessado_repository

    async def deletar(self, interessado_id: int) -> dict:            
        interessado = await self.__interessado_repository.deletar_interessado(interessado_id)
        return {
            "message": f"Interessado {interessado.id} deletado com sucesso."
        }


