from typing import List
from abc import ABC, abstractmethod
from src.models.entities.imovel import Pretensao

class PretensaoRepositoryInterface(ABC):

    @abstractmethod
    async def listar_pretensoes(self) -> List[Pretensao]: pass

    @abstractmethod
    async def inserir_pretensao(self, pretensao_info: dict) -> Pretensao: pass

    @abstractmethod
    async def visualizar_pretensao(self, pretensao_id: int) -> Pretensao: pass

    @abstractmethod
    async def atualizar_pretensao(self, pretensao_info: dict) -> Pretensao: pass

    @abstractmethod
    async def deletar_pretensao(self, pretensao_id: int) -> Pretensao: pass