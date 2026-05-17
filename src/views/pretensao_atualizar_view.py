from src.controllers.interfaces.pretensao_atualizar_controller import PretensaoAtualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class PretensaoAtualizarView:
    def __init__(self, controller: PretensaoAtualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_atualizar_pretensao(self, http_request: HttpRequest) -> HttpResponse:
        try:
            pretensao_data = {"id": http_request.param.get("pretensao_id"), "descricao": http_request.body.get("descricao")}
            response = await self.__controller.atualizar(pretensao_data)
            return HttpResponse(body=response, status_code=200)            
        except Exception as exception:
            error_handler(exception)