import os
import multiprocessing
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
from tqdm import tqdm

def compress_pdf(input_path, output_folder):
    try:
        with open(input_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            pdf_writer = PdfWriter()

            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            output_file_path = output_folder / input_path.relative_to(input_folder).parent / (input_path.stem + '.pdf')
            output_file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            print(f"Compressed: {input_path} -> {output_file_path}")
    except Exception as e:
        print(f"Error compressing {input_path}: {e}")

def process_folder(input_folder, output_folder):
    files = list(input_folder.glob('**/*.pdf'))
    with multiprocessing.Pool() as pool:
        list(pool.starmap(compress_pdf, [(file, output_folder) for file in files]))

if __name__ == "__main__":
    input_folder_name = input("Enter the input folder name: ")
    input_folder = Path(input_folder_name)

    if not input_folder.exists() or not input_folder.is_dir():
        print("Invalid input folder path.")
    else:
        output_folder_name = input_folder_name + "_compressed"
        output_folder = Path(output_folder_name)
        output_folder.mkdir(parents=True, exist_ok=True)
        process_folder(input_folder, output_folder)
