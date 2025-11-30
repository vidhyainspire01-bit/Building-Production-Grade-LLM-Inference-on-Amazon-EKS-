# GenAI Inference Gateway (FastAPI + Async + Redis + vLLM + OpenAI)

This is the unified LLM entrypoint for the organization.
All applications (CUE, SDLC Automation, InfraGuard) use this gateway.

## Features
- Async FastAPI inference
- Dynamic batching
- Redis caching
- Token streaming
- vLLM model serving
- OpenAI routing
- Retry & timeout handling
- Metrics via Prometheus
- Kubernetes-ready (EKS/AKS)
