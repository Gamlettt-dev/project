def log(filename=None):
    """
    Декоратор для логирования выполнения функций.

    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            # Формируем строку с входными параметрами
            inputs = f"Inputs: {args}, {kwargs}"

            try:
                result = func(*args, **kwargs)

                message = f"{func.__name__} ok\n"

                if filename:
                    with open(filename, 'a') as f:
                        f.write(message)
                else:
                    print(message, end='')

                return result

            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. {inputs}\n"

                if filename:
                    with open(filename, 'a') as f:
                        f.write(message)
                else:
                    print(message, end='')

                raise

        return wrapper

    return decorator


@log()
def divide(a, b):
    return a / b


divide(10, 2)
divide(10, 0)


#@log(filename="C:/Users/proje/mylog.txt")
#def divide(a, b):
#    return a / b
#divide(10, 2)
#divide(10, 0)
