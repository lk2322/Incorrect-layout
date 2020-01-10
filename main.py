import sys
from PySide2.QtWidgets import QApplication, QWidget, QFileDialog

from translate_utils import translate
from ui import Ui_Form


def translate_button_handler():
    """
    Переводит текст из одной раскладки в другую
    :return:
    """
    line = ui.lineEdit.text().lower()
    final = translate(line)

    ui.lineEdit_2.setText(final)
    ui.lineEdit_2.setReadOnly(True)
    return final

def save_button_handler():                                            
    """Сохраняет текст в файл"""
    # TODO возможность выбора файла для сохранения
    # with open('text.txt', 'w') as f:
    #    f.write(line)
    filename, _ = QFileDialog.getSaveFileName(filter=="txt files (.txt);;All Files ()")
    if filename != "":
        with open(filename, 'w') as f:
            text = translate(ui.lineEdit.text().lower())
            ui.lineEdit_2.setText(text)
            ui.lineEdit_2.setReadOnly(True)
            f.write(text)
            f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    ui.pushButton_3.clicked.connect(translate_button_handler)
    ui.pushButton_2.clicked.connect(save_button_handler)

    Form.show()
    sys.exit(app.exec_())
