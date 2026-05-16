from abc import ABC, abstractmethod

class ComentarioAtualizarControllerInterface(ABC):

    @abstractmethod
    async def atualizar(self, comentario_data: dict) -> dict: pass