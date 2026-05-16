from typing import List
from abc import ABC, abstractmethod
from src.models.entities.imovel import Comentario

class ComentarioRepositoryInterface(ABC):

    @abstractmethod
    async def listar_comentarios(self, imovel_id: int) -> List[Comentario]: pass

    @abstractmethod
    async def inserir_comentario(self, comentario_info: dict) -> Comentario: pass

    @abstractmethod
    async def visualizar_comentario(self, comentario_id: int) -> Comentario: pass

    @abstractmethod
    async def atualizar_comentario(self, comentario_info: dict) -> Comentario: pass

    @abstractmethod
    async def deletar_comentario(self, comentario_id: int) -> Comentario: pass