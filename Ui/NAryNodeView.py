from abc import ABC, abstractmethod

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QStyleOptionGraphicsItem, QWidget, QGraphicsItem, QMenu

from src.Ui.Arrow import Arrow
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
        self._click_start_pos = None
        self.out_arrows = []  # Arrows going out from this node
        self.in_arrows = []  # Arrows coming in to this Node
        # Context menu that will appear on right-clicking this Node
        self.context_menu = QMenu()  # not sure if should be empty!!!
        edit_action = self.context_menu.addAction("Edit")
        delete_action = self.context_menu.addAction("Delete")

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

    def add_to_out_arrows(self, arrow: Arrow) -> None:
        self.out_arrows.append(arrow)

    def add_to_in_arrows(self, arrow: Arrow) -> None:
        self.in_arrows.append(arrow)

    def set_controller(self, controller:SceneController)->None:
        self.controller = controller

    def mousePressEvent(self, event):
        self.setSelected(True)  # mark node as selected
        if hasattr(self, 'controller'):  # search if it has an attribute 'controller'
            self.controller.node_clicked(self)
        super().mousePressEvent(event)

    def contextMenuEvent(self, event):
        self.context_menu.exec(event.screenPos())

    def mousePressEvent(self, event):
        # Store initial position to detect movement
        self._click_start_pos = event.screenPos()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        # Check if mouse moved more than threshold so that would't be considered as a click on the node but as a drag and drop
        if self._click_start_pos is not None:
            distance = (event.screenPos() - self._click_start_pos).manhattanLength()
            if distance < 5:  # 5 pixels: treat as click
                print("Node clicked!")
                if hasattr(self, 'controller'):
                    self.controller.node_clicked(self)
        super().mouseReleaseEvent(event)