from typing import List
from src.models.interfaces.configuracao_repository import ConfiguracaoRepositoryInterface
from src.models.entities.imovel import Configuracao
from .interfaces.configuracao_listar_controller import ConfiguracaoListarControllerInterface

class ConfiguracaoListarController(ConfiguracaoListarControllerInterface):
    def __init__(self, configuracao_repository: ConfiguracaoRepositoryInterface) -> None:
        self.__configuracao_repository = configuracao_repository

    async def listar(self) -> dict:    
        configuracoes = await self.__buscar_configuracaos_db()
        response = self.__format_response(configuracoes)
        return response

    async def __buscar_configuracaos_db(self) -> List[Configuracao]:
        configuracoes = await self.__configuracao_repository.listar_configuracoes()
        return configuracoes

    def __format_response(self, configuracoes: List[Configuracao]) -> dict:
        formatted_configuracoes = [{ "id": configuracao.id, "descricao": configuracao.descricao, "quantidade": configuracao.quantidade} for configuracao in configuracoes]
        return {
            "type": "Configuracoes",
            "count": len(formatted_configuracoes),
            "configuracoes": formatted_configuracoes          
        }
