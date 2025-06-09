from typing import List, Optional
from models import DocumentCreate, DocumentUpdate, DocumentResponse


class DocumentManager:
    def __init__(self):
        """Inicializa o gerenciador com dados mockados incluindo IDs"""
        self.documents = [
            {"id": 1, "title": "Dom Casmurro", "type": "Livro", "extension": "pdf"},
            {"id": 2, "title": "O Cortiço", "type": "Livro", "extension": "epub"},
            {"id": 3, "title": "Revista Veja - Janeiro 2024", "type": "Revista", "extension": "pdf"},
            {"id": 4, "title": "Manual de Python", "type": "Manual", "extension": "pdf"},
            {"id": 5, "title": "Artigo Científico - IA na Educação", "type": "Artigo", "extension": "docx"},
            {"id": 6, "title": "Tese de Mestrado - Algoritmos", "type": "Tese", "extension": "pdf"},
            {"id": 7, "title": "Jornal Folha de São Paulo", "type": "Jornal", "extension": "pdf"},
            {"id": 8, "title": "Harry Potter e a Pedra Filosofal", "type": "Livro", "extension": "epub"},
            {"id": 9, "title": "Relatório Anual 2023", "type": "Relatório", "extension": "xlsx"},
            {"id": 10, "title": "Apresentação - Projeto Final", "type": "Apresentação", "extension": "pptx"}
        ]
        self.next_id = 11  # Próximo ID disponível
    
    def list_documents(self, type_filter: Optional[str] = None, 
                      extension_filter: Optional[str] = None, 
                      skip: int = 0, limit: int = 100) -> List[dict]:
        """Lista documentos com filtros opcionais e paginação"""
        filtered_docs = self.documents.copy()
        
        # Aplicar filtros
        if type_filter:
            filtered_docs = [doc for doc in filtered_docs if doc["type"].lower() == type_filter.lower()]
        
        if extension_filter:
            filtered_docs = [doc for doc in filtered_docs if doc["extension"].lower() == extension_filter.lower()]
        
        # Aplicar paginação
        return filtered_docs[skip:skip + limit]
    
    def get_document(self, doc_id: int) -> Optional[dict]:
        """Busca documento por ID"""
        for doc in self.documents:
            if doc["id"] == doc_id:
                return doc
        return None
    
    def create_document(self, document: DocumentCreate) -> dict:
        """Insere um novo documento"""
        new_doc = {
            "id": self.next_id,
            "title": document.title,
            "type": document.type,
            "extension": document.extension
        }
        self.documents.append(new_doc)
        self.next_id += 1
        return new_doc
    
    def update_document(self, doc_id: int, document: DocumentUpdate) -> Optional[dict]:
        """Atualiza um documento existente"""
        for doc in self.documents:
            if doc["id"] == doc_id:
                if document.title is not None:
                    doc["title"] = document.title
                if document.type is not None:
                    doc["type"] = document.type
                if document.extension is not None:
                    doc["extension"] = document.extension
                return doc
        return None
    
    def delete_document(self, doc_id: int) -> bool:
        """Deleta um documento"""
        for i, doc in enumerate(self.documents):
            if doc["id"] == doc_id:
                self.documents.pop(i)
                return True
        return False
    
    def count_documents(self) -> int:
        """Retorna o número total de documentos"""
        return len(self.documents)


# Instância global do gerenciador
document_manager = DocumentManager() 