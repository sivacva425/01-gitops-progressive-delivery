from fastapi import FastAPI
from prometheus_client import make_asgi_app, Counter, Histogram

app = FastAPI(title="AI Kubernetes Agent")
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

REQUEST_COUNT = Counter('flask_http_request_total', 'Total HTTP Requests', ['status'])

@app.get("/healthz")
def health_check():
    REQUEST_COUNT.labels(status='200').inc()
    return {"status": "healthy"}
