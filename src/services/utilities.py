def error_to_list (err: str) -> list:
    return [i.strip() for i in err.split('\n')]