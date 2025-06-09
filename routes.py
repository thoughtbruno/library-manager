from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models import DocumentCreate, DocumentUpdate, DocumentResponse

router = APIRouter()


@router.get("/documents", response_model=List[DocumentResponse])
async def get_documents(
    skip: int = Query(0, ge=0, description="Número de registros para pular"),
    limit: int = Query(100, ge=1, le=1000, description="Limite de registros para retornar"),
    type: Optional[str] = Query(None, description="Filtrar por tipo"),
    extension: Optional[str] = Query(None, description="Filtrar por extensão")
):
    """
    Rota para listar todos os documentos com filtros opcionais
    """
    # TODO: Implementar listagem de documentos
    pass


@router.get("/documents/{document_id}", response_model=DocumentResponse)
async def get_document(document_id: int):
    """
    Rota para buscar um documento por ID
    """
    # TODO: Implementar busca de documento por ID
    pass


@router.post("/documents", response_model=DocumentResponse, status_code=201)
async def create_document(document: DocumentCreate):
    """
    Rota para criar um novo documento
    """
    # TODO: Implementar criação de documento
    pass


@router.put("/documents/{document_id}", response_model=DocumentResponse)
async def update_document(document_id: int, document: DocumentUpdate):
    """
    Rota para atualizar um documento existente
    """
    # TODO: Implementar atualização de documento
    pass


@router.delete("/documents/{document_id}")
async def delete_document(document_id: int):
    """
    Rota para deletar um documento
    """
    # TODO: Implementar exclusão de documento
    pass 