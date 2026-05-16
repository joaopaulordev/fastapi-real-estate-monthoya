from abc import ABC, abstractmethod

class ComentarioInserirControllerInterface(ABC):

    @abstractmethod
    async def inserir(self, comentario_data: dict) -> dict: pass