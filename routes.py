from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models import DocumentCreate, DocumentUpdate, DocumentResponse
from document_manager import document_manager

router = APIRouter()


@router.get("/documents", response_model=List[DocumentResponse])
async def get_documents(
    skip: int = Query(0, ge=0, description="Número de registros para pular"),
    limit: int = Query(100, ge=1, le=1000, description="Limite de registros para retornar"),
    type: Optional[str] = Query(None, description="Filtrar por tipo"),
    extension: Optional[str] = Query(None, description="Filtrar por extensão")
):
    """
    Lista todos os documentos com filtros opcionais e paginação
    """
    return document_manager.list_documents(
        type_filter=type, 
        extension_filter=extension, 
        skip=skip, 
        limit=limit
    )


@router.get("/documents/count")
async def count_documents():
    """
    Retorna o número total de documentos
    """
    count = document_manager.count_documents()
    return {"total": count}


@router.get("/documents/{document_id}", response_model=DocumentResponse)
async def get_document(document_id: int):
    """
    Busca um documento por ID (índice)
    """
    document = document_manager.get_document(document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Documento não encontrado")
    return document


@router.post("/documents", response_model=DocumentResponse, status_code=201)
async def create_document(document: DocumentCreate):
    """
    Cria um novo documento
    """
    new_document = document_manager.create_document(document)
    return new_document


@router.put("/documents/{document_id}", response_model=DocumentResponse)
async def update_document(document_id: int, document: DocumentUpdate):
    """
    Atualiza um documento existente
    """
    updated_document = document_manager.update_document(document_id, document)
    if not updated_document:
        raise HTTPException(status_code=404, detail="Documento não encontrado")
    return updated_document


@router.delete("/documents/{document_id}")
async def delete_document(document_id: int):
    """
    Deleta um documento
    """
    success = document_manager.delete_document(document_id)
    if not success:
        raise HTTPException(status_code=404, detail="Documento não encontrado")
    return {"message": "Documento deletado com sucesso"} 