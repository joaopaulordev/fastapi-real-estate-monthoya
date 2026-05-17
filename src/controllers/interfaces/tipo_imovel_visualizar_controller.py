from abc import ABC, abstractmethod

class TipoImovelVisualizarControllerInterface(ABC):

    @abstractmethod
    async def visualizar(self, tipo_imovel_id: int) -> dict: pass