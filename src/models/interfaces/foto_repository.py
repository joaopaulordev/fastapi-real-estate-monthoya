from typing import List
from abc import ABC, abstractmethod
from src.models.entities.imovel import Foto

class FotoRepositoryInterface(ABC):

    @abstractmethod
    async def listar_fotos(self, imovel_id: int) -> List[Foto]: pass

    @abstractmethod
    async def inserir_foto(self, foto_info: dict) -> None: pass

    @abstractmethod
    async def deletar_foto(self, foto_id: int) -> Foto: pass