import os
from docx_utils import format_documents

def main():
    # Указываем папку с документами
    input_folder = "documents"
    output_folder = "formatted_documents"

    # Создаем папку для сохранения обработанных документов
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Запускаем форматирование
    format_documents(input_folder, output_folder)

if __name__ == "__main__":
    main()
