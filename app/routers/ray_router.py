import os

import ray
from dotenv import load_dotenv
from fastapi import APIRouter

from ..square_number.square_number import square_number

router = APIRouter(
    prefix="/ray",
    tags=["ray"],
)


def get_ray_address() -> str:
    load_dotenv()
    ray_address = os.getenv('RAY_CLUSTER_ADDRESS')
    if ray_address is None:
        raise ValueError("RAY_CLUSTER_ADDRESS environment variable not set.")

    return ray_address


def initialize_ray() -> None:
    ray_address = get_ray_address()
    print(f"Connecting to Ray cluster at {ray_address}...")
    ray.init(ray_address)
    print(f"Connected to Ray cluster at {ray_address}.")


@router.get("/")
def health() -> str:
    return "Ray OK"


@router.post("/square_sync")
def square_sync(x: int) -> int:
    if not ray.is_initialized():
        initialize_ray()

    @ray.remote
    def square_number_ray(num: int) -> int:
        return square_number(num)

    future = square_number_ray.remote(x)
    result = ray.get(future)

    return result
