# 📚 Library Manager

Sistema simples em **Python + FastAPI** com interface HTML estática para gerenciar documentos de uma biblioteca.

---

## 🏗️ Stack

- **Python 3.13**
- **FastAPI** + **Uvicorn** (backend REST)
- **Pydantic** (modelos)
- **HTML + CSS + JavaScript vanilla** (frontend)
- **CORS Middleware** habilitado para desenvolvimento

---

## 🚀 Como rodar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Inicie o servidor:

```bash
python main.py
```

  * O backend sobe em `http://localhost:8000`.
  * A interface web é servida em `http://localhost:8000/`.
  * Documentação Swagger em `http://localhost:8000/docs`.

---

## 🌐 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET    | `/` | Serve o arquivo `index.html` (interface web). |
| GET    | `/documents` | Lista documentos. Aceita filtros, paginação. |
| GET    | `/documents/count` | Retorna quantidade total de documentos. |
| GET    | `/documents/{id}` | Retorna documento pelo `id`. |
| POST   | `/documents` | Cria documento. |
| PUT    | `/documents/{id}` | Atualiza documento existente. |
| DELETE | `/documents/{id}` | Exclui documento pelo `id`. |

### 🔍 Detalhes

#### `GET /documents`

Query params:

| Param | Tipo | Padrão | Descrição |
|-------|------|--------|-----------|
| `skip` | `int` | `0` | Quantidade de registros a pular. |
| `limit` | `int` | `100` | Máximo de registros a retornar. |
| `type` | `str` | – | Filtra pelo tipo (Livro, Revista…). |
| `extension` | `str` | – | Filtra pelo formato (pdf, epub…). |

Resposta `200 OK`:
```json
[
  {
    "id": 1,
    "title": "Dom Casmurro",
    "type": "Livro",
    "extension": "pdf"
  }
]
```

#### `POST /documents`

Body (JSON):
```json
{
  "title": "Nome do documento",
  "type": "Livro",
  "extension": "pdf"
}
```
Resposta `201 Created` retorna o documento com `id` gerado.

#### `PUT /documents/{id}`

Body (JSON – todos opcionais):
```json
{
  "title": "Novo título",
  "type": "Revista",
  "extension": "epub"
}
```
Resposta `200 OK` devolve documento atualizado.

#### `DELETE /documents/{id}`

Resposta `200 OK`:
```json
{"message": "Documento deletado com sucesso"}
```

---

## 🖥️ Interface Web (`index.html`)

A página permite:

1. **Listar** documentos em tabela.
2. **Adicionar** documento via formulário.
3. **Editar** (carrega dados no formulário e envia `PUT`).
4. **Deletar** com confirmação.
5. **Filtrar** por tipo e extensão.
6. Exibe **total** de documentos (chama `/documents/count`).

Use o console do navegador para ver logs de debug caso algo não funcione.

---

## ⚙️ Estrutura do projeto

```
├── document_manager.py   # Lógica e dados mockados
├── main.py               # Configuração FastAPI + CORS + rotas
├── routes.py             # Endpoints REST
├── models.py             # Modelos Pydantic
├── index.html            # Interface estática
├── requirements.txt
└── README.md             # Este arquivo
```

---

## 🛡️ Observações de segurança

- CORS liberado para todas as origens apenas em **desenvolvimento**.
- Em produção, restrinja `allow_origins` para domínios confiáveis.

---

## 📄 Licença

Projeto educacional – use livremente.
