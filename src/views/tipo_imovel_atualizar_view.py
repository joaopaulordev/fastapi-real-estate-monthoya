from src.controllers.interfaces.tipo_imovel_atualizar_controller import TipoImovelAtualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class TipoImovelAtualizarView:
    def __init__(self, controller: TipoImovelAtualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_atualizar_tipo_imovel(self, http_request: HttpRequest) -> HttpResponse:
        try:
            tipo_imovel_data = {"id": http_request.param.get("tipo_imovel_id"), "descricao": http_request.body.get("descricao")}
            response = await self.__controller.atualizar(tipo_imovel_data)
            return HttpResponse(body=response, status_code=200)            
        except Exception as exception:
            error_handler(exception)