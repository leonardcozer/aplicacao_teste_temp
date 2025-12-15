import logging

from fastapi import APIRouter, HTTPException

from app.modules.customer.schemas import (
    CustomerMaintenanceRequest,
    CustomerMaintenanceResponse
)
from app.core.exceptions import BadRequestError

logger = logging.getLogger("api")


router = APIRouter(prefix="/api", tags=["customer maintenance"])


@router.post(
    "/new_directory",
    response_model=CustomerMaintenanceResponse,
    status_code=201,
    summary="Criar novo diretório",
    description="Cria um novo diretório para o cliente no servidor e disco especificados",
    responses={
        201: {"description": "Diretório criado com sucesso"},
        400: {"description": "Dados inválidos"},
        500: {"description": "Erro interno do servidor"},
    }
)
async def new_directory(request: CustomerMaintenanceRequest):
    """
    Cria um novo diretório para o cliente
    
    - **codigo_cliente**: Código do cliente (obrigatório)
    - **servidor_destino**: Servidor de destino (obrigatório)
    - **disco_destino**: Disco de destino (obrigatório)
    """
    try:
        logger.info(f"Criando diretório para cliente {request.codigo_cliente} no servidor {request.servidor_destino}")
        
        # TODO: Implementar lógica de criação de diretório
        # Por enquanto retorna resposta de sucesso
        return CustomerMaintenanceResponse(
            message="Diretorio criado com sucesso",
            status_code=201,
            data={
                "Servidor": request.servidor_destino,
                "Disco": request.disco_destino,
                "Codigo": request.codigo_cliente
            }
        )
    except BadRequestError as e:
        logger.warning(f"Erro de validação ao criar diretório: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Erro ao criar diretório: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")


@router.post(
    "/permission",
    response_model=CustomerMaintenanceResponse,
    status_code=201,
    summary="Aplicar permissões",
    description="Aplica permissões no diretório do cliente",
    responses={
        201: {"description": "Permissões aplicadas com sucesso"},
        400: {"description": "Dados inválidos"},
        500: {"description": "Erro interno do servidor"},
    }
)
async def permission(request: CustomerMaintenanceRequest):
    """
    Aplica permissões no diretório do cliente
    
    - **codigo_cliente**: Código do cliente (obrigatório)
    - **servidor_destino**: Servidor de destino (obrigatório)
    - **disco_destino**: Disco de destino (obrigatório)
    """
    try:
        logger.info(f"Aplicando permissões para cliente {request.codigo_cliente} no servidor {request.servidor_destino}")
        
        # TODO: Implementar lógica de aplicação de permissões
        # Por enquanto retorna resposta de sucesso
        return CustomerMaintenanceResponse(
            message="Diretorio criado com sucesso",
            status_code=201,
            data={
                "Servidor": request.servidor_destino,
                "Disco": request.disco_destino,
                "Codigo": request.codigo_cliente
            }
        )
    except BadRequestError as e:
        logger.warning(f"Erro de validação ao aplicar permissões: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Erro ao aplicar permissões: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")