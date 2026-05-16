from abc import ABC, abstractmethod

class FinalidadeInserirControllerInterface(ABC):

    @abstractmethod
    async def inserir(self, finalidade_data: dict) -> dict: pass