from abc import ABC, abstractmethod

class PretensaoListarControllerInterface(ABC):

    @abstractmethod
    async def listar(self) -> dict: pass
