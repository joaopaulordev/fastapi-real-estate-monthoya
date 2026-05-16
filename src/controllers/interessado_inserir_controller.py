from src.models.interfaces.interessado_repository import InteressadoRepositoryInterface
from .interfaces.interessado_inserir_controller import InteressadoInserirControllerInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from src.models.entities.imovel import Interessado

class InteressadoInserirController(InteressadoInserirControllerInterface):
    def __init__(self, interessado_repository: InteressadoRepositoryInterface) -> None:
        self._interessado_repository = interessado_repository

    async def inserir(self, interessado_data: dict) -> dict:
        self._validate_interessado_data(interessado_data)
        interessado = await self.__inserir_interessado(interessado_data)
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
        
    
    async def __inserir_interessado(self, interessado_data: dict) -> Interessado:
        interessado = await self._interessado_repository.inserir_interessado(interessado_data)
        return interessado


    def __format__response(self, interessado: Interessado) -> dict:
        formatted_interessado = { "id": interessado.id, "nome": interessado.nome, "email": interessado.email, "telefone": interessado.telefone, "estado": interessado.estado, "cidade": interessado.cidade, "imovel_id": interessado.imovel_id }
        return {
            "type": "Interessado",
            "count": 1,
            "attributes": formatted_interessado
        }