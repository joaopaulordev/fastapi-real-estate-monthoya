from src.errors.error_handler import error_handler
from src.controllers.interfaces.imovel_listar_controller import ImovelListarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class ImovelListarView:
    def __init__(self, controller: ImovelListarControllerInterface) -> None:
        self.__controller = controller

    async def handle_listar_imoveis(self, http_request: HttpRequest) -> HttpResponse:
        try:
            ativo = http_request.body.get("ativo")
            pretensao = http_request.body.get("pretensao")
            finalidade = http_request.body.get("finalidade")
            tipo_imovel = http_request.body.get("tipo_imovel")
            lancamento = http_request.body.get("lancamento")
            destaque = http_request.body.get("destaque")
            valor_inicial = http_request.body.get("valor_inicial")
            valor_final = http_request.body.get("valor_final")

            body_response = await self.__controller.listar(
                ativo=ativo,
                pretensao=pretensao,
                finalidade=finalidade,
                tipo_imovel=tipo_imovel,
                lancamento=lancamento,
                destaque=destaque,
                valor_inicial=valor_inicial,
                valor_final=valor_final
            )
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
