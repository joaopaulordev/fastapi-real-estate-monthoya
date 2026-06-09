from src.models.interfaces.configuracao_repository import ConfiguracaoRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from .interfaces.configuracao_atualizar_controller import ConfiguracaoAtualizarControllerInterface
from src.models.entities.imovel import Configuracao

class ConfiguracaoAtualizarController(ConfiguracaoAtualizarControllerInterface):
    def __init__(self, configuracao_repository: ConfiguracaoRepositoryInterface) -> None:
        self._configuracao_repository = configuracao_repository

    async def atualizar(self, configuracao_data: dict) -> dict:
        self._validate_configuracao_data(configuracao_data)
        configuracao = await self.__atualizar_configuracao(configuracao_data)
        return self.__format__response(configuracao)

    def _validate_configuracao_data(self, configuracao_data: dict) -> None:
        quantidade = configuracao_data["quantidade"]
        if quantidade < 2:
            raise HttpBadRequestError("Quantidade deve ser maior que 1.")        
        

    async def __atualizar_configuracao(self, configuracao_data: dict) -> Configuracao:
        return await self._configuracao_repository.atualizar_configuracao(configuracao_data)

    def __format__response(self, configuracao: Configuracao) -> dict:
        formatted_configuracao = { "id": configuracao.id, "descricao": configuracao.descricao, "quantidade": configuracao.quantidade }
        return {
            "type": "Configuracao",
            "count": 1,
            "configuracao": formatted_configuracao
        }