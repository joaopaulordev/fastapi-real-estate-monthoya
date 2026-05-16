from abc import ABC, abstractmethod

class InteressadoInserirControllerInterface(ABC):

    @abstractmethod
    async def inserir(self, interessado_data: dict) -> dict: pass