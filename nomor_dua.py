import pandas as pd

data = {
    "Nama": ["Mahasiswa 1", "Mahasiswa 2", "Mahasiswa 3"],
    "Algoritma dan Struktur Data 2": [90, 50, 65],
    "Matematika Numerik": [80, 60, 70]
}

df = pd.DataFrame(data)

print("Data Mahasiswa:")
print(df)

rata_rata_mata_kuliah = df[["Algoritma dan Struktur Data 2", "Matematika Numerik"]].mean()
print("\nRata-rata nilai untuk setiap mata kuliah:")
print(rata_rata_mata_kuliah)

df["Rata-rata nilai"] = df[["Algoritma dan Struktur Data 2", "Matematika Numerik"]].mean(axis=1)
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(df[["Nama", "Rata-rata nilai"]])