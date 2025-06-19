from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QWidget, QPushButton, QMenu

from src.Ui.StartNodeView import StartNodeView
from src.model.StartProcess import StartProcess


class ToolBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # add button for adding nodes TODO put in class toolsBox
        self.button = QPushButton('add', self)
        self.button.setToolTip('Add nodes')
        #self.button.move(100, 70)
        #self.button.clicked.connect(self.on_click)
        self.setMinimumSize(100, 50)
        # Dropdown menu
        nodes_menu = QMenu(self)
        start_node = nodes_menu.addAction("Start Node")
        start_node.triggered.connect(self.handle_start_node)

        process_node = nodes_menu.addAction("Process Node")
        process_node.triggered.connect(self.handle_process_node)

        end_node = nodes_menu.addAction("End Node")
        end_node.triggered.connect(self.handle_end_node)

        question_node = nodes_menu.addAction("Question Node")
        question_node.triggered.connect(self.handle_question_node)
        self.button.setMenu(nodes_menu)

    def handle_start_node(self)->None:
        print("handle_start_node")
        task_start_node = StartProcess("u3", "StartProcess", "Beggining of forkflow", [], "")
        start_node = StartNodeView(40, 30, task_start_node)
        #self.parent.add_to_list(task_start_node)
        self.scene.addItem(start_node)

    def handle_process_node(self)->None:
        print("handle_process_node")

    def handle_end_node(self)->None:
        print("handle_end_node")

    def handle_question_node(self)->None:
        print("handle_question_node")