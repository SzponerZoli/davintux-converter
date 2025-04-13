import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                            QWidget, QFileDialog)
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Davintux Converter")
        self.setGeometry(100, 100, 300, 150)
        self.selected_file = None
        
        # Create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create first button
        button1 = QPushButton("Convert to DR format", self)
        button1.clicked.connect(self.button1_clicked)
        layout.addWidget(button1)

        # Create file select button
        button2 = QPushButton("Select File", self)
        button2.clicked.connect(self.select_file)
        layout.addWidget(button2)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "All Files (*)"
        )
        if file_name:
            self.selected_file = file_name
            print(f"Selected file: {self.selected_file}")

    def button1_clicked(self):
        if self.selected_file:
            command = f'ffmpeg -i "{self.selected_file}" -c:v prores_ks -profile:v 3 -qscale:v 9 -acodec pcm_s16le "{self.selected_file}.mov"'
            os.system(command)
        else:
            print("Please select a file first!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())