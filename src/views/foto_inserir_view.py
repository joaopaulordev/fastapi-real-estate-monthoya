from src.controllers.interfaces.foto_inserir_controller import FotoInserirControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class FotoInserirView:
    def __init__(self, controller: FotoInserirControllerInterface) -> None:
        self.__controller = controller

    async def handle_inserir_foto(self, http_request: HttpRequest) -> HttpResponse:
        try:            
            foto_data = http_request.body
            await self.__controller.inserir(foto_data)
            return None
        except Exception as exception:
            error_handler(exception)