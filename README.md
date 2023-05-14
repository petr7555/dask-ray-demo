## How to run:

- install dependencies: `poetry install`
- run Dask cluster: `docker compose up -d`
- run Ray cluster: `ray start --head`
  - (later stop with `ray stop`)
- run server: `uvicorn app.main:app --reload`

### Run Ray Jobs

#### Using CLI

- `ray job submit --address ray://localhost:10001 -- python script.py`

#### Using Python SDK

- `python submit_ray_job.py`

### Remote cluster

- start Ray cluster in GCP: `ray up -y config.yaml`
- optionally, open dashboard: `ray dashboard config.yaml`, then go to [http://localhost:8265](http://localhost:8265)
- execute script: `ray submit config.yaml script.py`
- delete Ray cluster in GCP: `ray down -y config.yaml`

## Useful URLs:

- Dask dashboard is available at [http://localhost:8787](http://localhost:8787).
- Ray dashboard is available at [http://localhost:8265](http://localhost:8265).
- Interactive API docs (Swagger UI) are available at [http://localhost:8000/docs](http://localhost:8000/docs).
- Alternative API docs are available at [http://localhost:8000/redoc](http://localhost:8000/redoc).

## Generate presentation

- `npm install`
- `npm run build:pdf`
