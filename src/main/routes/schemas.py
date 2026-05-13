from pydantic import BaseModel
from typing import Optional, List

class ImovelSchema(BaseModel):
    descricao: str
    valor: float

    class Config:
        from_attributes = True


class BuscaImovelSchema(BaseModel):
    valor_inicial: float
    valor_final: float

    class Config:
        from_attributes = True