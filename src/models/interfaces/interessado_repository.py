from typing import List
from abc import ABC, abstractmethod
from src.models.entities.imovel import Interessado

class InteressadoRepositoryInterface(ABC):

    @abstractmethod
    async def listar_interessados(self, imovel_id: int) -> List[Interessado]: pass

    @abstractmethod
    async def inserir_interessado(self, interessado_info: dict) -> Interessado: pass

    @abstractmethod
    async def visualizar_interessado(self, interessado_id: int) -> Interessado: pass

    @abstractmethod
    async def atualizar_interessado(self, interessado_info: dict) -> Interessado: pass

    @abstractmethod
    async def deletar_interessado(self, interessado_id: int) -> Interessado: pass