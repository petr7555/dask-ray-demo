import time


def square_number(x: int) -> int:
    print(f"Sleeping for {x} seconds...")
    time.sleep(x)
    print(f"Done sleeping for {x} seconds.")
    return x * x
