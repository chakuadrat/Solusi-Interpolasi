import numpy as np
import matplotlib.pyplot as plt

def get_user_input():
    x_data = []
    y_data = []
    
    n = int(input("Masukkan jumlah data: "))
    
    for i in range(n):
        x = float(input(f"Masukkan nilai tegangan ke-{i+1} (kg/mm^2): "))
        y = float(input(f"Masukkan nilai waktu patah ke-{i+1} (jam): "))
        x_data.append(x)
        y_data.append(y)
    
    return np.array(x_data), np.array(y_data)

# Implementasi Interpolasi Polinom Lagrange
def lagrange_interpolation(x, y, x_interp):
    def L(k, x):
        terms = [(x - x[j])/(x[k] - x[j]) for j in range(len(x)) if j != k]
        return np.prod(terms, axis=0)
    
    return sum(y[k] * L(k, x_interp) for k in range(len(x)))

# Implementasi Interpolasi Polinom Newton
def newton_interpolation(x, y, x_interp):
    def divided_diff(x, y):
        n = len(y)
        coef = np.zeros([n, n])
        coef[:,0] = y
        
        for j in range(1,n):
            for i in range(n-j):
                coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
                
        return coef[0, :] 
    
    def newton_polynomial(coef, x_data, x):
        n = len(x_data) - 1
        p = coef[n]
        for k in range(1,n+1):
            p = coef[n-k] + (x -x_data[n-k])*p
        return p
    
    coef = divided_diff(x, y)
    return newton_polynomial(coef, x, x_interp)

# Fungsi utama
def main():
    """Fungsi utama untuk menjalankan program."""
    print("\nNisrina Azka Salsabila")
    print("21120122130057")
    print("Metode Numerik - Kelas C")
    print("Teknik Komputer")

    while True:
        print("\nPenyelesaian Interpolasi")
        print("\nSelamat datang! Silahkan pilih penyelesaian yang anda inginkan pada menu dibawah ini:")
        print("1. Polinom Lagrange")
        print("2. Polinom Newton")
        print("3. Keluar")

        pilihan = int(input("Masukkan pilihan Anda (1-3): "))

        if pilihan == 3:
            print("Terima kasih! Program berakhir.")
            break
        elif pilihan not in [1, 2]:
            print("Pilihan tidak valid, silahkan pilih kembali.")
            continue

        x_data, y_data = get_user_input()

        # Membuat range untuk x_interp
        x_interp = np.linspace(5, 40, 100)

        if pilihan == 1:
            # Menghitung hasil interpolasi dengan Lagrange
            y_interp = lagrange_interpolation(x_data, y_data, x_interp)
            metode = "Lagrange"
        elif pilihan == 2:
            # Menghitung hasil interpolasi dengan Newton
            y_interp = newton_interpolation(x_data, y_data, x_interp)
            metode = "Newton"

        # Plotting
        plt.figure(figsize=(12, 6))
        plt.plot(x_data, y_data, 'o', label='Data points')
        plt.plot(x_interp, y_interp, label=f'Interpolasi Polinom {metode}')
        plt.legend()
        plt.xlabel('Tegangan (x) [kg/mm^2]')
        plt.ylabel('Waktu Patah (y) [jam]')
        plt.title(f'Interpolasi Polinom {metode}')
        plt.show()

if __name__ == "__main__":
    main()
