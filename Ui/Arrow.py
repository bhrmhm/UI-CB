import math

from PyQt5.QtCore import QPointF, QRectF
from PyQt5.QtGui import QPainter, QPen, QBrush, QPolygonF, QPainterPath, QPainterPathStroker
from PyQt5.QtWidgets import QWidget, QGraphicsItem
from PyQt5.QtCore import Qt


class Arrow(QGraphicsItem):
    def __init__(self, start_node:QGraphicsItem, end_node:QGraphicsItem):
        super().__init__()
        self._start_node = start_node
        self._end_node = end_node
        #self.setZValue(-1) #set under nodes
        self.setFlags(QGraphicsItem.ItemIsSelectable)

    def boundingRect(self) -> QRectF:
        start = self.mapFromItem(self._start_node, self._start_node.boundingRect().center())
        #end = self._end_node.boundingRect()
        #end_top_center = self.mapFromItem(self._end_node, QPointF(end.center().x(), end.top()))
        end = self.mapFromItem(self._end_node, self._end_node.boundingRect().center())
        return QRectF(start, end).normalized().adjusted(-15, -15, 15, 15)


    def paint(self, painter: QPainter, option, widget=None):
        #TODO figure out how to draw the arrow outside of node's bounding - make it cleaner
        start_point = self.mapFromItem(self._start_node, self._start_node.boundingRect().center())
        end_point = self.mapFromItem(self._end_node, self._end_node.boundingRect().center())
        start_rect = self._start_node.boundingRect()
        start_down_center = self.mapFromItem(self._start_node, QPointF(start_rect.center().x(), start_rect.bottom()))
        end_rect = self._end_node.boundingRect()
        end_top_center = self.mapFromItem(self._end_node, QPointF(end_rect.center().x(), end_rect.top()))

        direction = end_top_center - start_down_center
        length = math.sqrt(direction.x() ** 2 + direction.y() ** 2)
        # Normalize direction
        direction_unit = QPointF(direction.x() / length, direction.y() / length)
        angle = math.atan2(-direction.y(), direction.x())

        # Arrowhead settings
        arrow_size = 10
        # Compute new tip point for arrow (before node edge)
        arrow_tip = end_top_center - direction_unit * 14
        arrow_p1 = end_top_center + QPointF(
            math.sin(angle - math.pi / 6) * arrow_size,
            math.cos(angle - math.pi / 6) * arrow_size
        )
        arrow_p2 = end_top_center + QPointF(
            math.sin(angle + math.pi / 6) * arrow_size,
            math.cos(angle + math.pi / 6) * arrow_size
        )

        arrow_head = QPolygonF([arrow_p1, arrow_p2, end_top_center])

        # Draw line
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(int(start_down_center.x()), int(start_down_center.y()), int(end_top_center.x()), int(end_top_center.y()))

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



