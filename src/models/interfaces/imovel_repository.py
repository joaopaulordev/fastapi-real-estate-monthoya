from typing import List
from abc import ABC, abstractmethod
from src.models.entities.imovel import Imovel

class ImovelRepositoryInterface(ABC):

    @abstractmethod
    async def inserir_caracteristicas_imovel(self, imovel_info: dict) -> Imovel: pass

    @abstractmethod
    async def deletar_caracteristicas_imovel(self, imovel_info: dict) -> None: pass

    @abstractmethod
    async def atualizar_caracteristicas_imovel(self, imovel_info: dict) -> Imovel: pass

    @abstractmethod
    async def listar_imoveis(self, imovel_info: dict) -> List[Imovel]: pass

    @abstractmethod
    async def inserir_imovel(self, imovel_info: dict) -> Imovel: pass

    @abstractmethod    
    async def visualizar_imoveis(self, imovel_id: int, count_view: bool): pass

    @abstractmethod
    async def atualizar_imovel(self, imovel_info: dict, clean_loc: bool) -> Imovel: pass

    @abstractmethod    
    async def deletar_imovel(self, imovel_id: int) -> None: pass 

    @abstractmethod
    async def buscar_imoveis_similares(self, imovel_id: int) -> List[Imovel]: pass