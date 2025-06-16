from abc import ABC, abstractmethod

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QStyleOptionGraphicsItem, QWidget, QGraphicsItem

from src.Ui.SceneController import SceneController
from src.model import Task


class NodeView(QGraphicsItem):
    """Abstract class for each Node graphic"""
    def __init__(self, x:int, y:int, task:Task):
    #def __init__(self, id:str,name:str, x:int, y:int):
        super().__init__(parent=None)
        self.setPos(x, y)  # This positions the item in the scene
        self._x = x
        self._y = y
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable
        )

        self.setAcceptHoverEvents(True)
        self._task = task
        self.setToolTip(self._task.get_description())
        self.out_arrows = []  # Arrows going out from this node
        self.in_arrows = []

    def execute(self):
        raise NotImplementedError("Each node must implement its own execute()")

    def boundingRect(self) -> QRectF:
        # Placeholder, overridden by each subclass
        return QRectF(0, 0, 100, 50)

    def paint(self, painter, option, widget=None):
        raise NotImplementedError("Each node must implement its own paint()")

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_task(self)->Task:
        return self._task

    def set_controller(self, controller:SceneController)->None:
        self.controller = controller

    def mousePressEvent(self, event):
        print("Node clicked!")
        self.setSelected(True) # mark node as selected
        if hasattr(self, 'controller'): #search if it has an attribute 'controller'
            self.controller.node_clicked(self)
        super().mousePressEvent(event)



