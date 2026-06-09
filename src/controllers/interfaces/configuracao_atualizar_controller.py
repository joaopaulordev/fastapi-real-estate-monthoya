from abc import ABC, abstractmethod

class ConfiguracaoAtualizarControllerInterface(ABC):

    @abstractmethod
    async def atualizar(self, configuracao_data: dict) -> dict: pass