# Recursive-PDF-Compressor
A Python script to recursively comperes PDFs in a nested directory. 

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/pdf-compressor.git
    ```

2. Navigate to the directory:
    ```bash
    cd pdf-compressor
    ```

3. Install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:
    ```bash
    python comp.py
    ```
    You will be prompted to enter the input folder name. Provide the name of the folder containing the PDF files you want to compress.

5. The compressed PDF files will be saved in a separate directory named `input_folder_name_compressed`, preserving the original folder structure.

## Requirements
- Python 3.x
- PyPDF2
- tqdm
