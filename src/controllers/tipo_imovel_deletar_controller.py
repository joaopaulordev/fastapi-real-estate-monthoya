from src.models.interfaces.tipo_imovel_repository import TipoImovelRepositoryInterface
from .interfaces.tipo_imovel_deletar_controller import TipoImovelDeletarControllerInterface


class TipoImovelDeletarController(TipoImovelDeletarControllerInterface):
    def __init__(self, tipo_imovel_repository: TipoImovelRepositoryInterface) -> None:
        self.__tipo_imovel_repository = tipo_imovel_repository

    async def deletar(self, tipo_imovel_id: int) -> dict:    
        tipo_imovel = await self.__tipo_imovel_repository.deletar_tipo_imovel(tipo_imovel_id)
        return {
            "message": f"Tipo Imóvel {tipo_imovel.descricao} deletado com sucesso."
        }


