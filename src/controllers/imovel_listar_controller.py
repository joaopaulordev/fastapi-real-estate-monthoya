from typing import Dict, List
from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.models.entities.imovel import Imovel
from .interfaces.imovel_listar_controller import ImovelListarControllerInterface

class ImovelListarController(ImovelListarControllerInterface):
    def __init__(self, imovel_repository: ImovelRepositoryInterface) -> None:
        self.__imovel_repository = imovel_repository

    async def listar(self, valor_inicial: float, valor_final: float) -> Dict:
        imoveis = await self.__busca_imoveis_db(valor_inicial, valor_final)
        response = self.__format_response(imoveis)
        return response

    async def __busca_imoveis_db(self, valor_inicial: float, valor_final: float) -> List[Imovel]:
        imoveis = await self.__imovel_repository.listar_imoveis(valor_inicial, valor_final) 
        return imoveis

    def __format_response(self, imoveis: List[Imovel]) -> Dict:
        formatted_imoveis = [{ "descricao": imovel.descricao, "valor": imovel.valor, "id": imovel.id } for imovel in imoveis]
        return {
            "data": {
                "type": "Imoveis",
                "count": len(formatted_imoveis),
                "attributes": formatted_imoveis
            }
        }
