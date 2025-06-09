from datetime import datetime
from models import DocumentResponse

# Lista mockada de documentos de biblioteca
mock_documents = [
    {"title": "Dom Casmurro", "type": "Livro", "extension": "pdf"},
    {"title": "O Cortiço", "type": "Livro", "extension": "epub"},
    {"title": "Revista Veja - Janeiro 2024", "type": "Revista", "extension": "pdf"},
    {"title": "Manual de Python", "type": "Manual", "extension": "pdf"},
    {"title": "Artigo Científico - IA na Educação", "type": "Artigo", "extension": "docx"},
    {"title": "Tese de Mestrado - Algoritmos", "type": "Tese", "extension": "pdf"},
    {"title": "Jornal Folha de São Paulo", "type": "Jornal", "extension": "pdf"},
    {"title": "Harry Potter e a Pedra Filosofal", "type": "Livro", "extension": "epub"},
    {"title": "Relatório Anual 2023", "type": "Relatório", "extension": "xlsx"},
    {"title": "Apresentação - Projeto Final", "type": "Apresentação", "extension": "pptx"}
]

def get_all_documents():
    """Retorna todos os documentos mockados"""
    return mock_documents

def filter_documents(type_filter: str = None, extension_filter: str = None, skip: int = 0, limit: int = 100):
    """Filtra documentos por tipo e/ou extensão com paginação"""
    filtered_docs = mock_documents.copy()
    
    # Aplicar filtros
    if type_filter:
        filtered_docs = [doc for doc in filtered_docs if doc["type"].lower() == type_filter.lower()]
    
    if extension_filter:
        filtered_docs = [doc for doc in filtered_docs if doc["extension"].lower() == extension_filter.lower()]
    
    # Aplicar paginação
    return filtered_docs[skip:skip + limit]