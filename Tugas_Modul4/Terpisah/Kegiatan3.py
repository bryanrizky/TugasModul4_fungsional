# Decorator untuk mengubah teks menjadi title case
def title_decorator(function):
    def wrapper():
        func_result = function()

        # Check if the result is a list
        if isinstance(func_result, list):
            make_title = ' '.join(map(str.title, func_result))
        else:
            make_title = func_result.title()

        print(make_title + " - Data is converted to title case")
        return make_title

    return wrapper

# Decorator untuk memisahkan setiap kata dalam string
def split_string_decorator(function):
    def wrapper():
        func_result = function()
        splitted_string = func_result.split()
        print(str(splitted_string) + " - Then data is splitted")
        return splitted_string

    return wrapper

# Fungsi say_hi
@split_string_decorator
@title_decorator
def say_hi():
    return 'hello there'

# Memanggil fungsi say_hi yang sudah di-decorate
result = say_hi()

# Mencetak hasil
print(result)
