from abc import ABC, abstractmethod

class ComentarioDeletarControllerInterface(ABC):

    @abstractmethod
    async def deletar(self, comentario_id: int) -> dict: pass