---
theme: uncover
paginate: true
---

# **Distributed computing in Python**

Petr Janík, 2023

---

# Motivation

- 😊 It's easy to develop POC ML algorithms locally on small data.
- 😓 It's hard to put them to production and/or run them on large data.

---
![bg opacity](computers.png)

<style scoped>
p {
  background-color: rgba(255, 255, 255, 0.5);
}
</style>

# Solution

Distributed computing

---

# Project intro

![width:50px height:50px](poetry-logo.svg) Poetry
![width:50px height:50px](fastapi-logo.svg) FastAPI

---

# **Dask.distributed**

_A lightweight library for distributed computing in Python._

<!-- _footer: https://distributed.dask.org/ -->

---

# How to install

```bash
poetry add dask distributed
```

---

# **Ray**

_Open-source unified compute framework that makes it easy to scale AI and Python workloads._

<!-- _footer: https://www.ray.io/ -->

---

# How to install

```bash
poetry add "ray[default]"
```

---

# Ray Client

Connects to a remote Ray cluster.

```python
ray.init("ray://localhost:10001")


@ray.remote
def square_number_ray(num: int) -> int:
    return square_number(num)


future = square_number_ray.remote(2)
result = ray.get(future)  # 4
```

<!-- _footer: https://docs.ray.io/en/latest/cluster/running-applications/job-submission/ray-client.html -->

---

# Ray Jobs

The recommended way to run a job on a Ray cluster.

<!-- _footer: https://docs.ray.io/en/latest/cluster/running-applications/job-submission/index.html -->

---

# Jobs CLI

```bash
ray job submit --address http://localhost:8265 -- python script.py
```

<!-- _footer: https://docs.ray.io/en/latest/cluster/running-applications/job-submission/quickstart.html -->

---

# Python SDK:

```python
client = JobSubmissionClient("http://localhost:8265")
job_id = client.submit_job(
    entrypoint="python script.py",
)
```

<!-- _footer: https://docs.ray.io/en/latest/cluster/running-applications/job-submission/sdk.html -->

---

# Thank you

Code + Slides: https://github.com/petr7555/dask-ray-demo
 
