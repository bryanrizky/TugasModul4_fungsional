def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    # Inner function untuk menghitung nilai M (gradien)
    def calculate_m(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return (y2 - y1) / (x2 - x1)

    # Menghitung nilai M (gradien)
    M = calculate_m(p1, p2)

    # Menghitung nilai C (konstanta)
    x, y = p1
    C = y - M * x

    # Membuat dan mengembalikan persamaan garis
    return f"y = {M:.2f}x + {C:.2f}"

# Titik A dan B
point_A = point(1, 3)
point_B = point(9, 0)

# Mencetak persamaan garis yang melalui titik A dan B
print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point_A, point_B))
