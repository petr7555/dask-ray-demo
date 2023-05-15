Preparation:

- `docker compose up -d`
- `uvicorn app.main:app --reload`

Presentation:

- Intro:
	- show presentation up to project intro
	- introduce project in code
	- run commands in Postman
- Dask:
	- show Dask in presentation
	- show Dask in code
	- show dask using Postman
- Ray:
	- show Ray in presentation
	- `ray start --head`
	- back to presentation
	- `ray job submit --address ray://localhost:10001 -- python script.py`
	- back to presentation
	- `python submit_ray_job.py`
	- `ray job logs <job_id>`
