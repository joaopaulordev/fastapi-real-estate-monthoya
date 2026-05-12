from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Imovel(Base):
    __tablename__ = "imoveis"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    descricao = Column("descricao", String, nullable=False)
    valor = Column("valor", Float, nullable=False)
    # fotos = relationship("Foto", backref="imovel", cascade="all, delete")

    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor        

    def __repr__(self):
        return f"Imovel [descricao={self.descricao}, valor={self.valor}]"



class Foto(Base):
    __tablename__ = "fotos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    caminho = Column("caminho", String, nullable=False)
    imovel = Column("imovel", ForeignKey("imoveis.id"))
    
    def __init__(self, caminho, imovel):
        self.caminho = caminho
        self.imovel = imovel

    def __repr__(self):
        return f"Foto [caminho={self.caminho}, imovel={self.imovel}]"