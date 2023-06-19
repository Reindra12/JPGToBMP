import os

folder_path = "dataset/mentah/bukan_mobil"
# folder_path = folder.replace(os.sep, '/')
# Mengubah nama gambar menjadi nomor urut

def rename_images(folder_path, new_folder_path):
    count = 1
    existing_filenames = set()

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            # Mengambil ekstensi file
            ext = os.path.splitext(filename)[1]

            # Nama baru untuk gambar
            new_filename = str(count) + ext

            while new_filename in existing_filenames:
                count += 1
                new_filename = str(count) + ext

            # Cek apakah nama gambar sudah ada
            if new_filename != filename:
                # Path gambar lama
                old_path = os.path.join(folder_path, filename)

                # Path gambar baru
                new_path = os.path.join(new_folder_path, new_filename)

                # Membuat folder baru jika belum ada
                os.makedirs(new_folder_path, exist_ok=True)

                # Mengubah nama gambar dan memindahkannya ke folder baru
                os.rename(old_path, new_path)
                print(f"{old_path} berhasil diubah menjadi {new_path}")

            existing_filenames.add(new_filename)
            count += 1

# Simpan nama gambar dalam file TXT
def save_image_names_to_txt(folder_path, txt_file_path):
    with open(txt_file_path, "w") as txt_file:
        existing_filenames = set()

        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg"):
                # Mengambil nama file tanpa ekstensi
                name = os.path.splitext(filename)[0]

                # Cek apakah nama file sudah ada
                if name in existing_filenames:
                    txt_file.write(filename + "\n")
                else:
                    existing_filenames.add(name)

    print(f"Nama-nama gambar yang sudah ada telah disimpan dalam file: {txt_file_path}")

# Folder baru untuk menyimpan file yang sudah direname
new_folder_path = "dataset/preprocessing/citra_negative"

# Panggil fungsi untuk mengubah nama gambar
rename_images(folder_path, new_folder_path)

# Path file TXT untuk menyimpan nama gambar
txt_file_path = "nama_gambar.txt"

# Panggil fungsi untuk menyimpan nama gambar dalam file TXT
save_image_names_to_txt(new_folder_path, txt_file_path)