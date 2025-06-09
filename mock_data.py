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
