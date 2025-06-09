from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from fastapi.responses import FileResponse
import os

app = FastAPI(
    title="Library Manager",
    version="1.0.0",
    description="Sistema de gerenciamento de biblioteca com operações CRUD para documentos",
    docs_url="/docs",  # URL do Swagger UI (padrão)
    redoc_url="/redoc",  # URL do ReDoc (padrão)
    openapi_url="/openapi.json",  # URL do schema OpenAPI (padrão)
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens em desenvolvimento
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os headers
)

# Incluir as rotas
app.include_router(router)


@app.get("/", response_class=FileResponse, include_in_schema=False)
async def serve_frontend():
    """Serve o arquivo index.html"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return FileResponse(os.path.join(base_dir, "index.html"))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 