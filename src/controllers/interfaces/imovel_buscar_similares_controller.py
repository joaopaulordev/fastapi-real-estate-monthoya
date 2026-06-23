from typing import Dict
from abc import ABC, abstractmethod

class ImovelBuscarSimilaresControllerInterface(ABC):

    @abstractmethod
    async def buscar_similares(self, imovel_id: int) -> Dict: pass
   