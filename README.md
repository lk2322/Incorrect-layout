# Incorrect layout
Переводит текст, написанный с неправильной раскладкой.
# Зависимости
Python 3, PySide2
# Использование
**Linux**
```
git clone https://github.com/lk2322/Incorrect-layout.git
cd Incorrect-layout
python main.py
```
**Windows**

Запустить exe
```
https://github.com/lk2322/Incorrect-layout/releases
```
Запустить main.py
```
git clone https://github.com/lk2322/Incorrect-layout.git
cd Incorrect-layout
python main.py
```
# Сборка
**Сборка exe**

Сборка возможна только в Windows
```
pip install pyinstaller
git clone https://github.com/lk2322/Incorrect-layout.git
cd Incorrect-layout
pyinstaller --onefile --noconsole --icon=2.ico main.py
```
В папке dist будет лежать exe

Features:
 - [ ] автоматическое определение вводимой раскладки
 - [x] возможность выбора файла для сохранения (через интерфейс)
 - [ ] возможность перевода текста без вызова графического интерфейса
 - [ ] иконка корретно добавляется в ресурсы при сборке .exe файла
 - [x] туториал по сборке проекта в исполняемый файл
 - [ ] .exe артефакт в релизах
 
