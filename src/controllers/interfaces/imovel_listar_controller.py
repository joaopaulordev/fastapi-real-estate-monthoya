from typing import Dict
from abc import ABC, abstractmethod

class ImovelListarControllerInterface(ABC):

    @abstractmethod
    async def listar(self, valor_inicial: float, valor_final: float, pretensao: int, finalidade: int, tipo_imovel: int, lancamento: bool, destaque: bool, ativo: bool) -> Dict:
        pass
