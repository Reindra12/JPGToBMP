from PIL import Image
import os


def convert_jpg_to_bmp(input_path, output_path):
    try:
        image = Image.open(input_path)
        image.save(output_path)
        print(f"{input_path} berhasil dikonversi menjadi {output_path}")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengonversi {input_path}: {str(e)}")


input_folder = "F:/AMIKOM/THESIS/program/JPGToBMP/dataset/mentah/mobil"
output_folder = "F:/AMIKOM/THESIS/program/JPGToBMP/dataset/bmp"

# Membuat folder output jika belum ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop melalui setiap file dalam folder input
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):
        # Path file input
        input_path = os.path.join(input_folder, filename)

        # Mengganti ekstensi file menjadi .bmp
        output_filename = os.path.splitext(filename)[0] + ".bmp"

        # Path file output
        output_path = os.path.join(output_folder, output_filename)

        # Mengonversi gambar JPG ke BMP
        convert_jpg_to_bmp(input_path, output_path)