from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from .interfaces.imovel_atualizar_controller import ImovelAtualizarControllerInterface
from src.models.entities.imovel import Imovel

class ImovelAtualizarController(ImovelAtualizarControllerInterface):
    def __init__(self, imovel_repository: ImovelRepositoryInterface) -> None:
        self._imovel_repository = imovel_repository

    async def atualizar(self, imovel_data: dict) -> dict:
        imovel = await self.__atualizar_imovel(imovel_data)
        return self.__format__response(imovel)

    async def __atualizar_imovel(self, imovel_data: dict) -> Imovel:
        return await self._imovel_repository.atualizar_imovel(imovel_data)

    def __format__response(self, imovel: Imovel) -> dict:
        formatted_imovel = { "id": imovel.id, "descricao": imovel.descricao, "ativo": imovel.ativo, "lancamento": imovel.lancamento, "destaque": imovel.destaque, "valor": imovel.valor, "visualizacoes": imovel.visualizacoes, "finalidade": imovel.finalidade, "tipo_imovel": imovel.tipo_imovel, "pretensao": imovel.pretensao, "estado": imovel.estado, "cidade": imovel.cidade, "endereco": imovel.endereco, "complemento": imovel.complemento, "sobre_imovel": imovel.sobre_imovel, "area_total": imovel.area_total, "area_construida": imovel.area_construida, "dormitorios": imovel.dormitorios, "banheiros": imovel.banheiros, "suites": imovel.suites, "vagas_garagem": imovel.vagas_garagem, "vagas_garagem_cobertas": imovel.vagas_garagem_cobertas, "vagas_garagem_descobertas": imovel.vagas_garagem_descobertas}
        return {
            "type": "Imóvel",
            "count": 1,
            "attributes": formatted_imovel
        }