from abc import ABC, abstractmethod

class PretensaoVisualizarControllerInterface(ABC):

    @abstractmethod
    async def visualizar(self, pretensao_id: int) -> dict: pass