from pydantic import BaseModel
from typing import Optional, List


class FinalidadeSchema(BaseModel):
    descricao: str
    
    class Config:
        from_attributes = True


class TipoImovelSchema(BaseModel):
    descricao: str
    
    class Config:
        from_attributes = True


class PretensaoSchema(BaseModel):
    descricao: str
    
    class Config:
        from_attributes = True


class ImovelSchema(BaseModel):
    descricao: Optional[str] = None
    ativo: Optional[bool] = None
    lancamento: Optional[bool] = None
    destaque: Optional[bool] = None
    valor: Optional[float] = None
    visualizacoes: Optional[int] = 0
    finalidade: Optional[int] = None
    tipo_imovel: Optional[int] = None
    pretensao: Optional[int] = None
    estado: Optional[int] = None 
    cidade: Optional[str] = None
    endereco: Optional[str] = None
    complemento: Optional[str] = None
    sobre_imovel: Optional[str] = None
    area_total: Optional[float] = None
    area_construida: Optional[float] = None 
    dormitorios: Optional[int] = None
    banheiros: Optional[int] = None
    suites: Optional[int] = None
    vagas_garagem: Optional[int] = None
    vagas_garagem_cobertas: Optional[int] = None
    vagas_garagem_descobertas: Optional[int] = None

    class Config:
        from_attributes = True


class BuscaImovelSchema(BaseModel):
    ativo: Optional[bool] = True
    pretensao: int
    finalidade: int
    tipo_imovel: int    
    lancamento: Optional[bool] = False
    destaque: Optional[bool] = False
    valor_inicial: float
    valor_final: float

    class Config:
        from_attributes = True


class ComentarioSchema(BaseModel):
    texto: str
    aprovado: Optional[bool] = False

    class Config:
        from_attributes = True


class InteressadoSchema(BaseModel):
    nome: str
    email: str
    telefone: str
    estado: int
    cidade: str

    class Config:
        from_attributes = True

class CaracteristicasSchema(BaseModel):
    caracteristicas_id: Optional[List[int]]

    class Config:
        from_attributes = True