from typing import List
from abc import ABC, abstractmethod
from src.models.entities.imovel import Finalidade

class FinalidadeRepositoryInterface(ABC):

    @abstractmethod
    async def listar_finalidades(self) -> List[Finalidade]: pass

    @abstractmethod
    async def inserir_finalidade(self, finalidade_info: dict) -> Finalidade: pass

    @abstractmethod
    async def visualizar_finalidade(self, finalidade_id: int) -> Finalidade: pass

    @abstractmethod
    async def atualizar_finalidade(self, finalidade_info: dict) -> Finalidade: pass

    @abstractmethod
    async def deletar_finalidade(self, finalidade_id: int) -> Finalidade: pass