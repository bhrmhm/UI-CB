import math

from PyQt5.QtCore import QPointF, QRectF
from PyQt5.QtGui import QPainter, QPen, QBrush, QPolygonF, QPainterPath, QPainterPathStroker, QPaintEvent
from PyQt5.QtWidgets import QWidget, QGraphicsItem
from PyQt5.QtCore import Qt

from src.Ui.NAryNodeView import NAryNodeView
from src.Ui.AtomicNodeView import AtomicNodeView
from src.tools.IDFactory import IDFactory


class Arrow(QGraphicsItem):
    #TODO change AtomicNodeView | NAryNodeView to NodeView
    def __init__(self, start_node:AtomicNodeView | NAryNodeView, end_node:AtomicNodeView | NAryNodeView, workflow_name:str):
        super().__init__()
        self._start_node = start_node
        self._end_node = end_node
        self._id = IDFactory().get_uri_id(workflow_name, "edge", start_node.get_name_task()+"-"+end_node.get_name_task())
        self.setZValue(-1) #set under nodes
        self._label = None #arrows exiting from a question node should have a label
        self.setFlags(QGraphicsItem.ItemIsSelectable)

    def boundingRect(self) -> QRectF:
        start = self.mapFromItem(self._start_node, self._start_node.boundingRect().center())
        #end = self._end_node.boundingRect()
        #end_top_center = self.mapFromItem(self._end_node, QPointF(end.center().x(), end.top()))
        end = self.mapFromItem(self._end_node, self._end_node.boundingRect().center())
        return QRectF(start, end).normalized().adjusted(-15, -15, 15, 15)


    def paint(self, painter: QPainter, option, widget=None):
        # Get start and end points
        start_rect = self._start_node.boundingRect()
        end_rect = self._end_node.boundingRect()
        # Check if the start node is on top of the end node or the opposite
        if self._start_node.scenePos().y() > self._end_node.scenePos().y():
            start_point = self.mapFromItem(self._start_node, QPointF(start_rect.center().x(), start_rect.top()))
            end_point = self.mapFromItem(self._end_node, QPointF(end_rect.center().x(), end_rect.bottom()))
            print("We are in: start.y>end.y")
        elif self._start_node.scenePos().y() < self._end_node.scenePos().y():
            start_point = self.mapFromItem(self._start_node, QPointF(start_rect.center().x(), start_rect.bottom()))
            end_point = self.mapFromItem(self._end_node, QPointF(end_rect.center().x(), end_rect.top()))
            print("We are in: start.y<end.y")
        else:
            # TODO  consider the x too - for now:
            start_point = self.mapFromItem(self._start_node, QPointF(start_rect.center().x(), start_rect.top()))
            end_point = self.mapFromItem(self._end_node, QPointF(end_rect.center().x(), end_rect.bottom()))
            print("We are in: else")


        arrow_size = 10
        angle = math.radians(30)
        theta = math.atan2(end_point.y()-start_point.y(), end_point.x()-start_point.x())
        x3 = end_point.x() - arrow_size * math.cos(theta-angle)
        y3 = end_point.y() - arrow_size * math.sin(theta-angle)
        x4 = end_point.x() - arrow_size * math.cos(theta+angle)
        y4 = end_point.y() - arrow_size * math.sin(theta+angle)
        arrow_head = QPolygonF([
            end_point,
            QPointF(x3, y3),
            QPointF(x4, y4),
            end_point
        ])

        # Draw line
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(int(start_point.x()), int(start_point.y()), int(end_point.x()),
                         int(end_point.y()))

        # Draw arrow head
        painter.setBrush(QBrush(Qt.black))
        painter.drawPolygon(arrow_head)




    def shape(self) -> QPainterPath:
        path = QPainterPath()
        start_point = self.mapFromItem(self._start_node, self._start_node.boundingRect().center())
        end_point = self.mapFromItem(self._end_node, self._end_node.boundingRect().center())
        path.moveTo(start_point)
        path.lineTo(end_point)
        stroker = QPainterPathStroker()
        stroker.setWidth(10)  # Tolerance width
        return stroker.createStroke(path)

    def get_start_task(self):
        return self._start_node.get_task()

    def get_end_task(self):
        return self._end_node.get_task()
    def get_id(self):
        return self._id
    def get_label(self):
        return self._label



