from typing import List
from sqlalchemy.orm import Session
from src.errors.types.http_not_found_error import HttpNotFoundError
from src.models.interfaces.configuracao_repository import ConfiguracaoRepositoryInterface
from src.models.entities.imovel import Configuracao

class ConfiguracaoRepository(ConfiguracaoRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.__db_session = db


    async def listar_configuracoes(self) -> List[Configuracao]:
        return self.__db_session.query(Configuracao).all()        

    

    async def atualizar_configuracao(self, configuracao_info: dict) -> Configuracao:
        try:
            configuracao = self.__db_session.query(Configuracao).filter(Configuracao.id == configuracao_info.get("id")).first()
            if not configuracao:
                raise HttpNotFoundError("Configuração não encontrada.")

            configuracao.quantidade = configuracao_info.get("quantidade")            
            self.__db_session.commit()
            
            return configuracao
        except Exception as exception:
            self.__db_session.rollback()
            raise exception