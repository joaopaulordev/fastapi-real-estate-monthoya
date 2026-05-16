from abc import ABC, abstractmethod

class InteressadoVisualizarControllerInterface(ABC):

    @abstractmethod
    async def visualizar(self, interessado_id: int) -> dict: pass