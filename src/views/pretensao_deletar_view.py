from src.errors.error_handler import error_handler
from src.controllers.interfaces.pretensao_deletar_controller import PretensaoDeletarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PretensaoDeletarView:
    def __init__(self, controller: PretensaoDeletarControllerInterface) -> None:
        self.__controller = controller

    async def handle_deletar_pretensao(self, http_request: HttpRequest) -> HttpResponse:
        try:
            pretensao_id = http_request.param.get("pretensao_id")
            body_response = await self.__controller.deletar(pretensao_id)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
