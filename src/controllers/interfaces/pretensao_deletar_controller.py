from abc import ABC, abstractmethod

class PretensaoDeletarControllerInterface(ABC):

    @abstractmethod
    async def deletar(self, pretensao_id: int) -> dict: pass