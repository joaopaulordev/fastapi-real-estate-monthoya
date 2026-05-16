from abc import ABC, abstractmethod

class ComentarioVisualizarControllerInterface(ABC):

    @abstractmethod
    async def visualizar(self, comentario_id: int) -> dict: pass