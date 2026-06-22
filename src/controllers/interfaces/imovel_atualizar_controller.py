from typing import Dict
from abc import ABC, abstractmethod

class ImovelAtualizarControllerInterface(ABC):

    @abstractmethod
    async def atualizar(self, imovel_data: dict, clean_loc: bool) -> dict: pass