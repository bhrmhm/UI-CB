from PyQt5.QtCore import QRectF, Qt, QPointF
from PyQt5.QtGui import QPainter, QBrush, QColor, QPolygonF
from PyQt5.QtWidgets import QStyleOptionGraphicsItem, QWidget

from src.Ui.NAryNodeView import NAryNodeView
from src.model.NAryNode import NAryTask
from src.model.Task import Task



class QuestionNodeView(NAryNodeView):
    def __init__(self, x:int, y:int, h:int, w:int,nAry:NAryTask):
        super().__init__(x,y,h, w, nAry)
        self._width = 120
        self._height = 70


    def boundingRect(self) -> QRectF:
        return QRectF(0,0, self._width, self._height)

    def paint(self, painter: QPainter, option, widget=None):
        w, h = self._width, self._height
        points = [
            QPointF(w * 0.25, 0),
            QPointF(w * 0.75, 0),
            QPointF(w, h * 0.5),
            QPointF(w * 0.75, h),
            QPointF(w * 0.25, h),
            QPointF(0, h * 0.5)
        ]
        hexagon = QPolygonF(points)
        # Draw hexagon
        painter.setBrush(QBrush(QColor(245, 245, 220)))
        painter.setPen(Qt.black)
        painter.drawPolygon(hexagon)

        # Draw centered text
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self._nAry.get_name())

    def execute(self):
        print(f"Executing ProcessNode {self._nAry.get_id()}")




