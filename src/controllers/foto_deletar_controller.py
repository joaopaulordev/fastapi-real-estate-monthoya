from src.errors.types.http_not_found_error import HttpNotFoundError
from src.models.interfaces.foto_repository import FotoRepositoryInterface
from .interfaces.foto_deletar_controller import FotoDeletarControllerInterface
import os

class FotoDeletarController(FotoDeletarControllerInterface):
    def __init__(self, foto_repository: FotoRepositoryInterface) -> None:
        self.__foto_repository = foto_repository

    async def deletar(self, foto_id: int) -> dict:            
        foto = await self.__foto_repository.deletar_foto(foto_id)

        if os.path.exists(foto.caminho):
            os.remove(foto.caminho)        
        else:
            raise HttpNotFoundError("Foto não encontrada no servidor.")
    
        return {
            "type": "Foto",
            "message": f"Foto {foto.id} deletada com sucesso.",
            "count": 1,
            "attributes": {
                "id": foto.id,
                "caminho": foto.caminho,
                "imovel_id": foto.imovel
            }
        }


