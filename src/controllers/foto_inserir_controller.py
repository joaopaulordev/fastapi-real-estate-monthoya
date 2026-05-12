from src.models.interfaces.foto_repository import FotoRepositoryInterface
from .interfaces.foto_inserir_controller import FotoInserirControllerInterface

class FotoInserirController(FotoInserirControllerInterface):
    def __init__(self, foto_repository: FotoRepositoryInterface) -> None:
        self._foto_repository = foto_repository

    async def inserir(self, foto_data: dict) -> None:        
        await self._foto_repository.inserir_foto(foto_data)

 