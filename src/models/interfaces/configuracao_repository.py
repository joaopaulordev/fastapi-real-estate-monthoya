from typing import List
from abc import ABC, abstractmethod
from src.models.entities.imovel import Configuracao

class ConfiguracaoRepositoryInterface(ABC):

    @abstractmethod
    async def listar_configuracoes(self) -> List[Configuracao]: pass

    @abstractmethod
    async def atualizar_configuracao(self, configuracao_info: dict) -> Configuracao: pass
