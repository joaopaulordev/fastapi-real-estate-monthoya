from typing import Dict
from abc import ABC, abstractmethod

class FotoInserirControllerInterface(ABC):

    @abstractmethod
    async def inserir(self, foto_data: Dict) -> None: pass