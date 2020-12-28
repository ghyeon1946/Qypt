from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QPixmap, QColor
from PyQt5.QtCore import Qt

class Canvas(QLabel):
    def __init__(self, size):
        super().__init__()
        
        self.size = size
        self.setPixmap(QPixmap(*size))
        self.setFixedSize(*size)
        
        # 그림판 초기화
        self.clear_canvas()
    
    # 그림 그릴 곳을 하얀색으로 칠하기
    def clear_canvas(self):
        painter = QPainter(self.pixmap())
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.drawRect(-100, -100, self.size[0]+100, self.size[1]+100)
        painter.end()
    
    # 마우스가 눌린 상태에서 움직이면 발생
    def mouseMoveEvent(self, e):
        painter = QPainter(self.pixmap())
        painter.setPen(QPen(QColor(0, 0, 0), 2))
        
        painter.drawPoint(e.x(), e.y())
        
        painter.end()
        
        # QLabel을 업데이트 해주는 함수
        self.repaint()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.Canvas = Canvas((1250, 700))
        self.setFixedSize(1280, 720)

        MainWidget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.Canvas)
        MainWidget.setLayout(layout)
        
        self.setCentralWidget(MainWidget)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    w = MainWindow()
    app.exec_()