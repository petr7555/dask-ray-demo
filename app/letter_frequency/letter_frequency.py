from pydantic import BaseModel


def count_letter_frequency(text: str) -> dict[str, int]:
    return {letter: text.count(letter) for letter in set(text)}


def reduce_letter_frequency(results: list[dict[str, int]]) -> dict[str, int]:
    def get_or_default(dictionary: dict[str, int], key: str) -> int:
        return dictionary.get(key, 0)

    return {k: sum([get_or_default(d, k) for d in results]) for k in set().union(*results)}


class LetterFrequencyModel(BaseModel):
    text: str
