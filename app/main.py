from fastapi import FastAPI

from .routers import dask_router, ray_router, sync_router

app = FastAPI()
app.include_router(sync_router.router)
app.include_router(dask_router.router)
app.include_router(ray_router.router)


@app.get("/")
@app.get("/health")
def health() -> str:
    return "App OK"
