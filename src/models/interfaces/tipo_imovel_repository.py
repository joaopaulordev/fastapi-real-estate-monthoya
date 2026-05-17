from typing import List
from abc import ABC, abstractmethod
from src.models.entities.imovel import TipoImovel

class TipoImovelRepositoryInterface(ABC):

    @abstractmethod
    async def listar_tipo_imovels(self) -> List[TipoImovel]: pass

    @abstractmethod
    async def inserir_tipo_imovel(self, tipo_imovel_info: dict) -> TipoImovel: pass

    @abstractmethod
    async def visualizar_tipo_imovel(self, tipo_imovel_id: int) -> TipoImovel: pass

    @abstractmethod
    async def atualizar_tipo_imovel(self, tipo_imovel_info: dict) -> TipoImovel: pass

    @abstractmethod
    async def deletar_tipo_imovel(self, tipo_imovel_id: int) -> TipoImovel: pass