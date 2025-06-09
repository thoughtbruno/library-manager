from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models import DocumentCreate, DocumentUpdate, DocumentResponse
from mock_data import get_all_documents, filter_documents

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
    return filter_documents(type_filter=type, extension_filter=extension, skip=skip, limit=limit)


@router.get("/documents/{document_id}", response_model=DocumentResponse)
async def get_document(document_id: int):
    """
    Rota para buscar um documento por ID
    """
    # TODO: Implementar busca por ID
    raise HTTPException(status_code=501, detail="Busca por ID não implementada")


@router.post("/documents", response_model=DocumentResponse, status_code=201)
async def create_document(document: DocumentCreate):
    """
    Rota para criar um novo documento
    """
    # TODO: Implementar criação de documento
    raise HTTPException(status_code=501, detail="Funcionalidade não implementada")


@router.put("/documents/{document_id}", response_model=DocumentResponse)
async def update_document(document_id: int, document: DocumentUpdate):
    """
    Rota para atualizar um documento existente
    """
    # TODO: Implementar atualização de documento
    raise HTTPException(status_code=501, detail="Funcionalidade não implementada")


@router.delete("/documents/{document_id}")
async def delete_document(document_id: int):
    """
    Rota para deletar um documento
    """
    # TODO: Implementar exclusão de documento
    raise HTTPException(status_code=501, detail="Funcionalidade não implementada") 