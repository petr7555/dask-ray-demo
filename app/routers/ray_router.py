from fastapi import APIRouter

router = APIRouter(
    prefix="/ray",
)


@router.get("/")
def healthcheck() -> str:
    return "Ray OK"
