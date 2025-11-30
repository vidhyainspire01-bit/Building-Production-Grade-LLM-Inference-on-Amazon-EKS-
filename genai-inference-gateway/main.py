from fastapi import FastAPI
from src.api.routes.llm import router as llm_router
from src.api.routes.health import router as health_router
from src.api.middleware.error_handler import register_exception_handlers
from src.api.middleware.logging_middleware import LoggingMiddleware
from src.api.middleware.tracing_middleware import TracingMiddleware

def create_app():
    app = FastAPI(title="GenAI Inference Gateway")

    # Register Middleware
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(TracingMiddleware)

    # Routes
    app.include_router(llm_router, prefix="/llm")
    app.include_router(health_router, prefix="/health")

    # Error handlers
    register_exception_handlers(app)

    return app

app = create_app()
