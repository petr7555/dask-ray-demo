## How to run:

- install dependencies: `poetry install`
- run workers: `docker compose up -d`
- run server: `poetry run uvicorn main:app --reload`

## Useful links:
- Dask dashboard is available at [http://localhost:8787](http://localhost:8787).
- Ray dashboard is available at [http://localhost:8265/](http://localhost:8265/).
- Interactive API docs (Swagger UI) are available at [http://localhost:8000/docs](http://localhost:8000/docs).
- Alternative API docs are available at [http://localhost:8000/redoc](http://localhost:8000/redoc).

## Generate presentation
- `npm install`
- `npm run build:pdf`
