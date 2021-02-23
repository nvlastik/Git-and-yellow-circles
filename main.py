from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys
from random import randint 


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pix = QPixmap(600, 600)
        self.label.setPixmap(self.pix)
        self.btn.clicked.connect(self.draw_circle)
        self.n = 0

    def draw_circle(self):
        x, y = [randint(10, 500) for i in range(2)]
        w = randint(10, 100)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor("yellow"))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, w)
        painter.end()
        self.update()


app = QApplication(sys.argv)
w = Test()
w.show()
sys.exit(app.exec_())