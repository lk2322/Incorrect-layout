import sys, os, os.path
import PySide
from PySide import QtCore, QtGui
from ui import Ui_Form
app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()



en_ru = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш',
    'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', '{': 'х', '}': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в',
    'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', """'""": 'э',
    '"': 'э', ':': 'ж', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '<': 'б', '>': 'ю',
    ' ': ' ', '/': '.', '?': ',', '&': '?'


}
ru_en = {'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[{', 'ъ': ']}', 'ф': 'a',
         'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l',
         'ж': ';:', 'э': '\'"', 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v',
         'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',<', 'ю': '.>', ' ': ' ', '.': '/', ',': '?', '?': '&'}


def trans():
    line = ui.lineEdit.text().lower()
    res = []
    for i in line:
        res.append(en_ru.get(i, ''))
    final = ''.join(res).capitalize()

    ui.lineEdit_2.setText(final)
    ui.lineEdit_2.setReadOnly(True)
    return final


def save():
    line = trans()
    f = open('text.txt', 'w')
    f.write(line)
    f.close()

ui.pushButton_3.clicked.connect(trans)
ui.pushButton_2.clicked.connect(save)


sys.exit(app.exec_())
