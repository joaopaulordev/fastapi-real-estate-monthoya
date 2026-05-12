from abc import ABC, abstractmethod

class FotoDeletarControllerInterface(ABC):

    @abstractmethod
    async def deletar(self, foto_id: int) -> dict: pass