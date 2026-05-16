from abc import ABC, abstractmethod

class FinalidadeAtualizarControllerInterface(ABC):

    @abstractmethod
    async def atualizar(self, finalidade_data: dict) -> dict: pass