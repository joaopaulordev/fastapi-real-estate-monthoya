from src.errors.error_handler import error_handler
from src.controllers.interfaces.pretensao_visualizar_controller import PretensaoVisualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PretensaoVisualizarView:
    def __init__(self, controller: PretensaoVisualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_visualizar_pretensao(self, http_request: HttpRequest) -> HttpResponse:
        try:
            pretensao_id = http_request.param.get("pretensao_id")
            body_response = await self.__controller.visualizar(pretensao_id)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
