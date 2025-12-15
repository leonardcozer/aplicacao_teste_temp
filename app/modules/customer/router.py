import logging
from typing import Generator

from hamcrest import none
from fastapi import APIRouter, Depends, Query, HTTPException

from app.modules.customer.schemas import ProdutoCreateRequest, ProdutoUpdateRequest, ProdutoResponse, ProdutoListResponse
from app.modules.customer.service import ProdutoService
from app.core.exceptions import NotFoundError, BadRequestError
from app.core.validators import (
    sanitize_search_term,
    sanitize_category,
    validate_page_params,
    validate_id
)

logger = logging.getLogger("api")


router = APIRouter(prefix="/produtos", tags=["customer maintenance"])


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
        return none
        #service.criar_produto(produto_request)
    except BadRequestError as e:
        logger.warning(f"Erro de validação ao criar produto: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Erro ao criar produto: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")