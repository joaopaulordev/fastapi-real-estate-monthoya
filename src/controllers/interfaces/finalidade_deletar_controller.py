from abc import ABC, abstractmethod

class FinalidadeDeletarControllerInterface(ABC):

    @abstractmethod
    async def deletar(self, finalidade_id: int) -> dict: pass