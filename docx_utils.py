import os
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_LINE_SPACING

def format_document(file_path, output_path):
    """
    Форматирует документ: шрифт, размер шрифта, межстрочный интервал.
    """
    doc = Document(file_path)

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            run.font.name = "Times New Roman"
            run.font.size = Pt(14)
        paragraph.paragraph_format.line_spacing = 1.5

    doc.save(output_path)
    print(f"Документ {file_path} успешно отформатирован!")

def format_documents(input_folder, output_folder):
    """
    Форматирует все .docx документы в указанной папке.
    """
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".docx"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            format_document(input_path, output_path)
