from src.models.interfaces.pretensao_repository import PretensaoRepositoryInterface
from .interfaces.pretensao_deletar_controller import PretensaoDeletarControllerInterface


class PretensaoDeletarController(PretensaoDeletarControllerInterface):
    def __init__(self, pretensao_repository: PretensaoRepositoryInterface) -> None:
        self.__pretensao_repository = pretensao_repository

    async def deletar(self, pretensao_id: int) -> dict:     
        pretensao = await self.__pretensao_repository.deletar_pretensao(pretensao_id)
        return {
            "message": f"Pretensão {pretensao.descricao} deletada com sucesso."
        }


