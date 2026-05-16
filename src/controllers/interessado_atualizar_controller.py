from src.models.interfaces.interessado_repository import InteressadoRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from .interfaces.interessado_atualizar_controller import InteressadoAtualizarControllerInterface
from src.models.entities.imovel import Interessado

class InteressadoAtualizarController(InteressadoAtualizarControllerInterface):
    def __init__(self, interessado_repository: InteressadoRepositoryInterface) -> None:
        self._interessado_repository = interessado_repository

    async def atualizar(self, interessado_data: dict) -> dict:
        self._validate_interessado_data(interessado_data)
        interessado = await self.__atualizar_interessado(interessado_data)
        return self.__format__response(interessado)

    def _validate_interessado_data(self, interessado_data: dict) -> None:
        nome = interessado_data.get("nome")
        if not nome:
            raise HttpBadRequestError("O campo 'nome' é obrigatório.")
        
        email = interessado_data.get("email")
        if not email:
            raise HttpBadRequestError("O campo 'email' é obrigatório.")
        
        telefone = interessado_data.get("telefone")
        if not telefone:
            raise HttpBadRequestError("O campo 'telefone' é obrigatório.")
        
        estado = interessado_data.get("estado")
        if not estado:
            raise HttpBadRequestError("O campo 'estado' é obrigatório.")
        
        cidade = interessado_data.get("cidade")
        if not cidade:
            raise HttpBadRequestError("O campo 'cidade' é obrigatório.")
        

    async def __atualizar_interessado(self, interessado_data: dict) -> Interessado:
        return await self._interessado_repository.atualizar_interessado(interessado_data)

    def __format__response(self, interessado: Interessado) -> dict:
        formatted_interessado = { "id": interessado.id, "nome": interessado.nome, "email": interessado.email, "telefone": interessado.telefone, "estado": interessado.estado, "cidade": interessado.cidade, "imovel_id": interessado.imovel_id }
        return {
            "type": "Interessado",
            "count": 1,
            "attributes": formatted_interessado
        }