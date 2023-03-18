from fastapi import APIRouter

from app.letter_frequency.letter_frequency import LetterFrequencyModel, count_letter_frequency
from app.square_number.square_number import square_number

router = APIRouter(
    prefix="/sync",
    tags=["sync"],
)


@router.get("/")
def health() -> str:
    return "Sync OK"


@router.post("/square_sync")
def square_sync(x: int) -> int:
    return square_number(x)


@router.post("/letter_frequency")
def letter_frequency(model: LetterFrequencyModel) -> dict:
    return count_letter_frequency(model.text)
