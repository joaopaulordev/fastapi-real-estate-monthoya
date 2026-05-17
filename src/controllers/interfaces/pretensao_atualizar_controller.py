from abc import ABC, abstractmethod

class PretensaoAtualizarControllerInterface(ABC):

    @abstractmethod
    async def atualizar(self, pretensao_data: dict) -> dict: pass