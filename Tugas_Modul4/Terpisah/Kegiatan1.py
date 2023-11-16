# Curry function
def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# High Order Function (HOF)
def kali_dengan(a):
    def inner(b):
        return a * b
    return inner

# Panggil menggunakan High Order Function (HOF)
hasil_hof = kali_dengan(5)(3)
print("Hasil menggunakan HOF:", hasil_hof)

# Panggil menggunakan currying
hasil_currying = perkalian(5)(3)
print("Hasil menggunakan Currying:", hasil_currying)
