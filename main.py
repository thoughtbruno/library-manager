from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Library Manager",
    version="1.0.0",
    description="Sistema de gerenciamento de biblioteca com operações CRUD para documentos",
    docs_url="/docs",  # URL do Swagger UI (padrão)
    redoc_url="/redoc",  # URL do ReDoc (padrão)
    openapi_url="/openapi.json",  # URL do schema OpenAPI (padrão)
)

# Incluir as rotas
app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 