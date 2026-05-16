from abc import ABC, abstractmethod

class FinalidadeVisualizarControllerInterface(ABC):

    @abstractmethod
    async def visualizar(self, finalidade_id: int) -> dict: pass