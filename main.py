
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path

def open_file():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, 'Select Files')
    message.setText('\n'.join(filenames))



def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open (path, 'wb') as file:
            file.write(b'')
        path.unlink()
    message.setText('Destraction Successful!')

app = QApplication([])
window = QWidget()
window.setWindowTitle("File Destroyer")
layout = QVBoxLayout()

description = QLabel('Select the file/s you want to destroy. <br> <font color="red"> Warning </font>: The file/s will be permanently  deleted from your system.')
layout.addWidget(description)

open_btn = QPushButton('Open Files')
open_btn.setToolTip("Open File")
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_file)

destroy_btn = QPushButton('Destroy Files')
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

message = QLabel('')
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()