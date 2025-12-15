import logging
from typing import Generator

from fastapi import APIRouter, Depends, Query, HTTPException

from app.modules.customer.schemas import (
    ProdutoCreateRequest, 
    ProdutoUpdateRequest, 
    ProdutoResponse, 
    ProdutoListResponse,
    DirectoryRequest,
    DirectoryResponse
)
from app.modules.customer.service import ProdutoService
from app.core.exceptions import NotFoundError, BadRequestError
from app.core.validators import (
    sanitize_search_term,
    sanitize_category,
    validate_page_params,
    validate_id
)

logger = logging.getLogger("api")


router = APIRouter(prefix="/api", tags=["customer maintenance"])


def get_produto_service() -> ProdutoService:
    """
    Dependency injection para ProdutoService
    TODO: Implementar injeção de dependência adequada com repository
    """
    # Por enquanto retorna None - precisa ser implementado
    # quando o repository estiver disponível
    return None


@router.post(
    "",
    response_model=ProdutoResponse,
    status_code=201,
    summary="Criar novo produto",
    responses={
        201: {"description": "Produto criado com sucesso"},
        400: {"description": "Dados inválidos"},
    }
)
async def criar_produto(
    produto_request: ProdutoCreateRequest,
    service: ProdutoService = Depends(get_produto_service)
):
    """
    Cria um novo produto
    
    - **nome**: Nome do produto (obrigatório)
    - **descricao**: Descrição do produto
    - **preco**: Preço do produto (obrigatório, deve ser > 0)
    - **quantidade**: Quantidade em estoque
    - **categoria**: Categoria do produto (obrigatório)
    """
    try:
        if service is None:
            raise HTTPException(status_code=503, detail="Serviço não disponível - repository não configurado")
        return service.criar_produto(produto_request)
    except BadRequestError as e:
        logger.warning(f"Erro de validação ao criar produto: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Erro ao criar produto: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")


@router.post(
    "/new_directory",
    response_model=DirectoryResponse,
    status_code=201,
    summary="Criar novo diretório",
    responses={
        201: {"description": "Diretório criado com sucesso"},
        400: {"description": "Dados inválidos"},
    }
)
async def new_directory(request: DirectoryRequest):
    """
    Cria um novo diretório para o cliente
    
    - **codigo_cliente**: Código do cliente (obrigatório)
    - **servidor_destino**: Servidor de destino (obrigatório)
    - **disco_destino**: Disco de destino (obrigatório)
    """
    try:
        logger.info(f"Criando diretório para cliente {request.codigo_cliente}")
        
        # TODO: Implementar lógica de criação de diretório
        # Por enquanto retorna resposta de sucesso
        return DirectoryResponse(
            message="Diretorio criado com sucesso",
            status_code=201,
            data={
                "Servidor": request.servidor_destino,
                "Disco": request.disco_destino,
                "Codigo": request.codigo_cliente
            }
        )
    except Exception as e:
        logger.error(f"Erro ao criar diretório: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")


@router.post(
    "/permission",
    response_model=DirectoryResponse,
    status_code=201,
    summary="Aplicar permissões",
    responses={
        201: {"description": "Permissões aplicadas com sucesso"},
        400: {"description": "Dados inválidos"},
    }
)
async def permission(request: DirectoryRequest):
    """
    Aplica permissões no diretório do cliente
    
    - **codigo_cliente**: Código do cliente (obrigatório)
    - **servidor_destino**: Servidor de destino (obrigatório)
    - **disco_destino**: Disco de destino (obrigatório)
    """
    try:
        logger.info(f"Aplicando permissões para cliente {request.codigo_cliente}")
        
        # TODO: Implementar lógica de aplicação de permissões
        # Por enquanto retorna resposta de sucesso
        return DirectoryResponse(
            message="Diretorio criado com sucesso",
            status_code=201,
            data={
                "Servidor": request.servidor_destino,
                "Disco": request.disco_destino,
                "Codigo": request.codigo_cliente
            }
        )
    except Exception as e:
        logger.error(f"Erro ao aplicar permissões: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")