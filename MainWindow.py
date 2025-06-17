import random

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QMainWindow, QPushButton, QVBoxLayout, QGridLayout, \
    QAction, QToolBar, QGraphicsScene, QGraphicsView, QSizePolicy, QMenu
from PyQt5.QtCore import Qt, QSize, QRectF
import sys

from src.Ui.Arrow import Arrow
from src.Ui.ComputationNodeView import ComputationNodeView
from src.Ui.EndNodeView import EndNodeView
from src.Ui.ProcessNodeView import ProcessNodeView
from src.Ui.QuestionNodeView import QuestionNodeView
from src.Ui.SceneController import SceneController
from src.Ui.StartNodeView import StartNodeView
from src.model.ComputationNode import ComputationNode
from src.model.EndProcess import EndProcess

from src.model.ProcessNode import ProcessNode
from src.model.QuestionNode import QuestionNode
from src.model.StartProcess import StartProcess
from src.model.Task import Task
from src.tools.IDFactory import IDFactory


#TODO Later do a cleaner MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._nodes:list = []
        self._edges:list[list] = [] # Edges list [first_node, last_node]

        self.setWindowTitle("Test")
        self.resize(800, 700)  # Width x Height in pixels

        self.pane_principal = QGridLayout()

        # Create graphics scene and view
        self.scene = QGraphicsScene()
        self.controller = SceneController(self.scene, self._nodes)
        self.view = QGraphicsView(self.scene)
        self.view.setMinimumSize(300, 350)
        self.scene.setSceneRect(0, 0, 600, 650)  # Optional, but good for space
        self.scene.setItemIndexMethod(QGraphicsScene.NoIndex) #disable clipping

        # Add graphics view to the grid (row=0, col=1)
        self.pane_principal.addWidget(self.view, 0, 1)

        #make a central widget where we put other elements on it
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        #ToolBar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        #menu bar TODO make a class for it
        button_action = QAction("Export to JSON",self)
        button_action.triggered.connect(self.exportToJSON)
        toolbar.addAction(button_action)
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        file_menu.addAction(button_action)

        #add button for adding nodes TODO put in class toolsBox
        self.button = QPushButton('add', self)
        self.button.setToolTip('Add nodes')
        self.button.move(100, 70)
        #self.button.clicked.connect(self.on_click)

        #Dropdown menu
        nodes_menu = QMenu(self)
        start_node = nodes_menu.addAction("Start Node")
        start_node.triggered.connect(self.handle_start_node)
        end_node = nodes_menu.addAction("End Node")
        end_node.triggered.connect(self.handle_end_node)
        process_node = nodes_menu.addAction("Process Node")
        process_node.triggered.connect(self.handle_process_node)
        question_node = nodes_menu.addAction("Question Node")
        question_node.triggered.connect(self.handle_question_node)
        computation_node = nodes_menu.addAction("Computation Node")
        computation_node.triggered.connect(self.handle_computation_node)
        self.button.setMenu(nodes_menu)


        ''''#list of options for nodes and hide it
        self.list_widget = QListWidget()
        self.list_widget.addItems(["Start Node","End Node","Process Node", "Question Node", "Computation Node", "Interaction Node"])
        self.list_widget.hide()
        self.list_widget.currentItemChanged.connect(self.index_changed)  # set event handler?
        self.list_widget.itemClicked'''
        #self.add_tooBar = ToolBar(self)

        vBox = QVBoxLayout()
        vBox.addStretch(1)  # Push content to the bottom
        #vBox.addWidget(self.add_tooBar)
        vBox.addWidget(self.button, alignment=Qt.AlignLeft | Qt.AlignBottom)
        self.pane_principal.addLayout(vBox, 0, 0, alignment=Qt.AlignBottom | Qt.AlignLeft)
        self.central_widget.setLayout(vBox)

        self.pane_principal.addWidget(menu)
        self.central_widget.setLayout(self.pane_principal)
        #exemple
        '''id = IDFactory().get_uri_id("name_to_be_defined", "start", "Start node")
        task_start_node = StartProcess(id, "StartProcess", "Beggining of forkflow", [], "")
        start_node = StartNodeView(0,0, task_start_node)
        self.add_to_list(task_start_node)
        self.scene.addItem(start_node)

        id = IDFactory().get_uri_id("name_to_be_defined", "question", "Question node")
        nAry_question_node = QuestionNode(id, "Question Node", "4<a?", ["4<a"], " ")
        question_node = QuestionNodeView(200, 200, 100, 50, nAry_question_node)
        self.add_to_list(nAry_question_node)
        self.scene.addItem(question_node)
        arrow1 = Arrow(start_node, question_node)
        print(arrow1._start_node)
        print(arrow1._end_node)
        self.scene.addItem(arrow1)'''



    def add_to_list(self,task:Task):
        self._nodes.append(task)


    def exportToJSON(self):
        print("export to JSON")

    # for now details by default + later the user should be able to change it
    def handle_start_node(self)->None:
        print("handle_start_node")
        id = IDFactory().get_uri_id("name_to_be_defined", "start", "Start node")
        task_start_node = StartProcess(id, "StartProcess", "Beggining of forkflow", [], "")
        print(id)
        start_node = StartNodeView(random.randint(0,100), random.randint(0,100), task_start_node)
        start_node.set_controller(self.controller)
        self.add_to_list(task_start_node)
        self.scene.addItem(start_node)
        print(self.controller.get_nodes())

    def handle_end_node(self)->None:
        print("handle_end_node")
        id = IDFactory().get_uri_id("name_to_be_defined", "end", "End node")
        print(id)
        task_end_node = EndProcess(id, "EndProcess", "End of forkflow", [], "")
        end_node = EndNodeView(random.randint(0,100), random.randint(0,100), task_end_node)
        end_node.set_controller(self.controller)
        self.add_to_list(task_end_node)
        self.scene.addItem(end_node)

    def handle_question_node(self)->None:
        print("handle_question_node")
        id = IDFactory().get_uri_id("name_to_be_defined", "question", "Question node")
        print(id)
        nAry_question_node = QuestionNode(id, "Question Node", "4<a?", ["4<a"], " ")
        question_node = QuestionNodeView(random.randint(0,100),random.randint(0,100), 100, 50, nAry_question_node)
        question_node.set_controller(self.controller)
        self.add_to_list(nAry_question_node)
        self.scene.addItem(question_node)


    def handle_process_node(self)->None:
        print("handle_process_node")
        id = IDFactory().get_uri_id("name_to_be_defined", "process", "Process node")
        print(id)
        task_process_node = ProcessNode(id, "ProcessNode", " a+b=a", ["a+b=a"]," ")
        process_node = ProcessNodeView(random.randint(0,100),random.randint(0,100), task_process_node)
        process_node.set_controller(self.controller)
        self.add_to_list(task_process_node)
        self.scene.addItem(process_node)

    def handle_computation_node(self)->None:
        print("handle_computation_node")
        id = IDFactory().get_uri_id("name_to_be_defined", "parallel1", "Parallel node")
        nAry_computation_node1 = ComputationNode(id, "Computation Node", "", ["print(\"parallel 1\")"], "p1")
        computation_node1 = ComputationNodeView(random.randint(0,100), random.randint(0,100), 100, 50, nAry_computation_node1)
        computation_node1.set_controller(self.controller)
        id = IDFactory().get_uri_id("name_to_be_defined", "parallel2", "Parallel node")
        nAry_computation_node2 = ComputationNode(id, "Computation Node", "", ["print(\"parallel 2\")"], "p1")
        computation_node2 = ComputationNodeView(random.randint(0,100), random.randint(0,100), 100, 50, nAry_computation_node2)
        computation_node2.set_controller(self.controller)
        self.scene.addItem(computation_node1)
        self.scene.addItem(computation_node2)
        self.add_to_list(nAry_computation_node1)
        self.add_to_list(nAry_computation_node2)













app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()