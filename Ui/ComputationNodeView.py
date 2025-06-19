from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QWidget

from src.Ui.NAryNodeView import NAryNodeView
from src.model.NAryNode import NAryTask


class ComputationNodeView(NAryNodeView):
    def __init__(self, x:int, y:int, h:int, w:int,nAry:NAryTask):
        super().__init__(x,y,h,w,nAry)
        #TODO later set fix h and w


    def boundingRect(self) -> QRectF:
        return QRectF(0, 0, 75, 40)

    def paint(self, painter: QPainter, option, widget=None):
        painter.setBrush(QBrush(QColor(128, 128, 128)))
        painter.drawEllipse(self.boundingRect())
        painter.drawText(self.boundingRect(), Qt.AlignCenter, "||")

    def execute(self):
        print(f"Executing ProcessNode {self.get_task().get_id()}")

    def handle_edit_info(self):
        print("Edit not possible for this node")
        # TODO a dialog box for this message