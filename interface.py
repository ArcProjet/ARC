import sys
from PyQt5.QtWidgets import *
from main import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Création du QLabel
        self.label = QLabel("Label de test")
        self.menubar = QMenuBar()
        self.menubar.addMenu(QMenu().addSection(QAction("f")))

        centralWidget = QWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.setMenuBar(self.menubar)
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)

    def write(self, text):
        self.label.setText(self.label.text() + text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.resize(1000,500)

    window.show()

    sys.exit(app.exec_())