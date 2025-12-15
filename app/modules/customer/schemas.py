"""
Schemas para Customer Maintenance
Define os DTOs (Data Transfer Objects) para operações de manutenção de clientes
"""
from pydantic import BaseModel, Field


class CustomerMaintenanceRequest(BaseModel):
    """DTO para requisição de operações de manutenção de cliente"""
    codigo_cliente: str = Field(..., description="Código do cliente")
    servidor_destino: str = Field(..., description="Servidor de destino")
    disco_destino: str = Field(..., description="Disco de destino")

    class Config:
        json_schema_extra = {
            "example": {
                "codigo_cliente": "100817",
                "servidor_destino": "cmaticfspg15",
                "disco_destino": "Contmatic2"
            }
        }


class CustomerMaintenanceResponse(BaseModel):
    """DTO para resposta de operações de manutenção de cliente"""
    message: str
    status_code: int
    data: dict

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Diretorio criado com sucesso",
                "status_code": 201,
                "data": {
                    "Servidor": "cmaticfspg15",
                    "Disco": "Contmatic2",
                    "Codigo": "100817"
                }
            }
        }
