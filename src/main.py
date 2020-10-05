def add(a: int, b: int) -> int or str:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return 'Bad value'
