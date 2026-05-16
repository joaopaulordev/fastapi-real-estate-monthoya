from src.controllers.interfaces.finalidade_atualizar_controller import FinalidadeAtualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class FinalidadeAtualizarView:
    def __init__(self, controller: FinalidadeAtualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_atualizar_finalidade(self, http_request: HttpRequest) -> HttpResponse:
        try:
            finalidade_data = {"id": http_request.param.get("finalidade_id"), "descricao": http_request.body.get("descricao")}
            response = await self.__controller.atualizar(finalidade_data)
            return HttpResponse(body=response, status_code=200)            
        except Exception as exception:
            error_handler(exception)