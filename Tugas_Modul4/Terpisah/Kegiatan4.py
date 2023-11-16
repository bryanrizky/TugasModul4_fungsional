import math

# Fungsi untuk translasi
def translasi(tx, ty):
    def transformasi(p):
        x, y = p
        new_x = x + tx
        new_y = y + ty
        return new_x, new_y
    return transformasi

# Fungsi untuk dilatasi
def dilatasi(sx, sy):
    def transformasi(p):
        x, y = p
        new_x = x * sx
        new_y = y * sy
        return new_x, new_y
    return transformasi

# Fungsi untuk rotasi
def rotasi(sudut):
    def transformasi(p):
        x, y = p
        sudut_rad = math.radians(sudut)
        new_x = x * math.cos(sudut_rad) - y * math.sin(sudut_rad)
        new_y = x * math.sin(sudut_rad) + y * math.cos(sudut_rad)
        return new_x, new_y
    return transformasi

# Contoh kasus
titik_awal = (3, 5)

# 1. Translasi dengan tx = 2 dan ty = -1
translasi_2_minus_1 = translasi(2, -1)
titik_setelah_translasi = translasi_2_minus_1(titik_awal)
print("Titik setelah translasi:", titik_setelah_translasi)

# 2. Dilatasi dengan sx = 2 dan sy = -1
dilatasi_2_minus_1 = dilatasi(2, -1)
titik_setelah_dilatasi = dilatasi_2_minus_1(titik_awal)
print("Titik setelah dilatasi:", titik_setelah_dilatasi)

# 3. Rotasi dengan sudut = 30 derajat
rotasi_30_derajat = rotasi(30)
titik_setelah_rotasi = rotasi_30_derajat(titik_awal)
print("Titik setelah rotasi:", titik_setelah_rotasi)
