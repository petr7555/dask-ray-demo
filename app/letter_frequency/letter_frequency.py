from pydantic import BaseModel


def count_letter_frequency(text: str) -> dict:
    return {letter: text.count(letter) for letter in set(text)}


def reduce_letter_frequency(results: list[dict[str, int]]) -> dict:
    return {k: sum([d[k] for d in results]) for k in set().union(*results)}


class LetterFrequencyModel(BaseModel):
    text: str
