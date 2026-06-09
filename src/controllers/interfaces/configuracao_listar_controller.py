from abc import ABC, abstractmethod

class ConfiguracaoListarControllerInterface(ABC):

    @abstractmethod
    async def listar(self) -> dict: pass
