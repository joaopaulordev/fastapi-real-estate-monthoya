from typing import List
from src.models.interfaces.foto_repository import FotoRepositoryInterface
from src.models.entities.imovel import Foto
from .interfaces.foto_listar_controller import FotoListarControllerInterface

class FotoListarController(FotoListarControllerInterface):
    def __init__(self, foto_repository: FotoRepositoryInterface) -> None:
        self.__foto_repository = foto_repository

    async def listar(self, imovel_id: int) -> dict:
        fotos = await self.__buscar_fotos_db(imovel_id)
        response = self.__format_response(fotos)
        return response

    async def __buscar_fotos_db(self, imovel_id: int) -> List[Foto]:
        fotos = await self.__foto_repository.listar_fotos(imovel_id)
        return fotos

    def __format_response(self, fotos: List[Foto]) -> dict:
        formatted_fotos = [{ "id": foto.id, "caminho": foto.caminho, "imovel_id": foto.imovel } for foto in fotos]
        return {
            "data": {
                "type": "Fotos",
                "count": len(formatted_fotos),
                "attributes": formatted_fotos
            }
        }
