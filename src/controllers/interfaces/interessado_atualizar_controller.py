from abc import ABC, abstractmethod

class InteressadoAtualizarControllerInterface(ABC):

    @abstractmethod
    async def atualizar(self, interessado_data: dict) -> dict: pass