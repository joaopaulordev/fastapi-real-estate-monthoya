from abc import ABC, abstractmethod

class PretensaoInserirControllerInterface(ABC):

    @abstractmethod
    async def inserir(self, pretensao_data: dict) -> dict: pass