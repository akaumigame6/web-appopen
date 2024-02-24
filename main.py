import sys
import PySide6.QtWidgets as Qw
import pyside_code as py

if __name__ == '__main__':
  app = Qw.QApplication(sys.argv)
  main_window = py.MainWindow()
  main_window.show()
  sys.exit(app.exec())