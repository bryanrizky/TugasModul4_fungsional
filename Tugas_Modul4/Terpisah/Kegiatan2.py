# Decorator function
def uppercase_decorator(function):
    def wrapper():
        func_result = function()
        return func_result.upper()
    return wrapper

# Fungsi say_hi
@uppercase_decorator
def say_hi():
    return 'hello there'

# Memanggil fungsi say_hi yang sudah di-decorate
result = say_hi()

# Mencetak hasil
print(result)
