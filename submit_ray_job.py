from ray.job_submission import JobSubmissionClient

from app.routers.ray_router import get_ray_address

ray_address = get_ray_address()

client = JobSubmissionClient(ray_address)
job_id = client.submit_job(
    entrypoint="python script.py",
)

print(job_id)
