import sys
from PySide6.QtWidgets import QApplication

from controllers.time_counter import TimeCounterController


if __name__ == '__main__':
    app = QApplication()

    window = TimeCounterController()
    window.show()

    sys.exit(app.exec())