import os

from dask.distributed import Client, Future
from dotenv import load_dotenv
from fastapi import APIRouter

from ..letter_frequency.letter_frequency import LetterFrequencyModel, count_letter_frequency, reduce_letter_frequency
from ..square_number.square_number import square_number

router = APIRouter(
    prefix="/dask",
    tags=["dask"],
)


def get_client() -> Client:
    load_dotenv()
    dask_address = os.getenv('DASK_CLUSTER_ADDRESS')
    if dask_address is None:
        raise ValueError("DASK_CLUSTER_ADDRESS environment variable not set.")

    print(f"Connecting to Dask cluster at {dask_address}...")
    dask_client = Client(dask_address)
    print(f"Connected to Dask cluster at {dask_address}.")

    return dask_client


client = get_client()
futures_refs = []


@router.get("/")
def health() -> str:
    return "Dask OK"


@router.post("/square_sync")
def square_sync(x: int) -> int:
    # By default dask assumes that functions are pure and therefore caches results.
    # To avoid this, we can either use `pure=False` or not store a reference to the future.
    future = client.submit(square_number, x)
    futures_refs.append(future)
    return future.result()


@router.post("/square")
def square(x: int) -> str:
    future = client.submit(square_number, x)
    # Dask holds results in the memory as long as we have a reference to the future.
    futures_refs.append(future)
    return future.key


@router.get("/square/status/{key}")
def square_status(key: str) -> str:
    future = Future(key)
    return future.status


@router.get("/square/result/{key}")
def square_result(key: str) -> int:
    future = Future(key)
    return future.result()


@router.post("/letter_frequency")
def letter_frequency(model: LetterFrequencyModel) -> dict:
    sentences = model.text.split(".")

    # send to multiple machines to count letter frequency in each sentence
    futures = client.map(count_letter_frequency, sentences)

    # gather results on this machine
    results = client.gather(futures)

    return reduce_letter_frequency(results)
