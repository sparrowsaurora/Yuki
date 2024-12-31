import os
from PyPDF2 import PdfReader
import voice_input, speech_output

def read_text(text):
    speech_output.speak(text)

def read_txt_file(file_path):
    """Reads a .txt file and returns its content."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_py_file(file_path):
    """Reads a .py file and returns its content."""
    return read_txt_file(file_path)

def read_md_file(file_path):
    """Reads a .md file and returns its content."""
    return read_txt_file(file_path)

def read_pdf_file(file_path):
    """Reads a .pdf file and returns its content."""
    text = ""
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def main():
    file_path = input("Enter the path to the file (.py, .txt, .md, .pdf): ")
    
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
        return

    extension = os.path.splitext(file_path)[1].lower()
    
    if extension == '.txt':
        content = read_txt_file(file_path)
    elif extension == '.py':
        content = read_py_file(file_path)
    elif extension == '.md':
        content = read_md_file(file_path)
    elif extension == '.pdf':
        content = read_pdf_file(file_path)
    else:
        print("Unsupported file type.")
        return

    read_text(content)

if __name__ == "__main__":
    main()
