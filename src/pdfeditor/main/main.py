from pdfeditor.main.edits.edit_selecter import select_editor
from pdfeditor.main.edits.editor import Editor
from pdfeditor.main.files.pdf_edit_list import PdfEditList

def main() -> None:
    selected_editor: type[Editor] = select_editor()

    pdf_files: list[str] = PdfEditList().get_pdf_list
    editor_instance: Editor = selected_editor(pdf_files)
    editor_instance.run()

if __name__ == "__main__": main()