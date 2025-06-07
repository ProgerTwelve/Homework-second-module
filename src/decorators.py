from typing import Any, Callable


def log(filename: str = None) -> Any:
    """Декоратор, который логирует начало и конец выполнения функции"""

    def decorator(func: Callable) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_data = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_data + "\n")
                else:
                    print(log_data)
                return result

            except Exception as e:
                log_data = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_data + "\n")
                else:
                    print(log_data)

            raise type(Exception).__name__

        return wrapper

    return decorator
