from abc import ABC, abstractmethod

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QStyleOptionGraphicsItem, QWidget, QGraphicsItem

from src.Ui.SceneController import SceneController
from src.model import Task
from src.model.NAryNode import NAryTask


class NAryNodeView(QGraphicsItem):
    """Abstract class for each Node graphic"""
    def __init__(self, x:int, y:int, h:int, w:int,nAry:NAryTask): #TODO change back later when you have the classes
        super().__init__()
        self._x = x
        self._y = y
        self.setPos(x, y)
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable
        )
        self._nAry = nAry
        self.setToolTip(self._nAry.get_description())
        self._height = h
        self._width = w
        self.setToolTip(self._nAry.get_description())

    def execute(self):
        raise NotImplementedError("Each node must implement its own execute()")

    def boundingRect(self) -> QRectF:
        # Placeholder, overridden by each subclass
        return QRectF(0,0, self._width, self._height)

    def paint(self, painter, option, widget=None):
        raise NotImplementedError("Each node must implement its own paint()")

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def get_nAry(self)->NAryTask:
        return self._nAry

    def set_controller(self, controller:SceneController)->None:
        self.controller = controller

    def mousePressEvent(self, event):
        self.setSelected(True)  # mark node as selected
        if hasattr(self, 'controller'):  # search if it has an attribute 'controller'
            self.controller.node_clicked(self)
        super().mousePressEvent(event)

