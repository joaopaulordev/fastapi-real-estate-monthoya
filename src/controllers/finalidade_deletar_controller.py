from src.errors.types.http_not_found_error import HttpNotFoundError
from src.models.interfaces.finalidade_repository import FinalidadeRepositoryInterface
from .interfaces.finalidade_deletar_controller import FinalidadeDeletarControllerInterface


class FinalidadeDeletarController(FinalidadeDeletarControllerInterface):
    def __init__(self, finalidade_repository: FinalidadeRepositoryInterface) -> None:
        self.__finalidade_repository = finalidade_repository

    async def deletar(self, finalidade_id: int) -> dict:     
        finalidade = await self.__finalidade_repository.deletar_finalidade(finalidade_id)
        return {
            "message": f"Finalidade {finalidade.descricao} deletada com sucesso."
        }


