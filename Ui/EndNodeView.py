from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QStyleOptionGraphicsItem, QWidget

from src.Ui.NodeView import NodeView
from src.model.Task import Task


class EndNodeView(NodeView):
    def __init__(self, x: int, y: int, task: Task):
        super().__init__(x,y, task)

    def boundingRect(self) -> QRectF:
        return QRectF(0, 0, 120, 50)

    def paint(self, painter: QPainter, option, widget=None):
        painter.setBrush(QBrush(QColor(255, 0, 0)))
        painter.drawEllipse(self.boundingRect())
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self._task.get_name())

    def execute(self):
        print(f"Executing ProcessNode {self.get_task().get_id()}")


