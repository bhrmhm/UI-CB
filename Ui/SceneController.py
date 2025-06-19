class SceneController:
    def __init__(self, scene, nodes:list, workflow_name:str):
        self._scene = scene
        self._nodes = nodes
        self._edges = [] #List of arrows
        self._workflow_name = workflow_name
        self._first_node= None #first node clicked
        self._second_node = None #second node clicked

    def node_clicked(self, node):
        from src.Ui.Arrow import Arrow # to avoid circular import
        print("Clicked:", node, "Pos:", node.pos(), "Parent:", node.parentItem())
        if self._first_node is None:
            self._first_node = node
            print("First node clicked")
        else: #second node clicked: draw an arrow
            self._second_node = node
            print("Second node clicked")
            if self._first_node != self._second_node:
                arrow = Arrow(self._first_node, self._second_node, self._workflow_name)
                self._first_node.add_to_out_arrows(arrow)
                self._first_node.get_task().add_successor(self._second_node.get_task())
                self._second_node.add_to_in_arrows(arrow)
                self._scene.addItem(arrow)
                self._edges.append(arrow)
                print("succs of first node: ", self._first_node.get_task().get_successors())
            self._first_node = None

    def get_scene(self):
        return self._scene

    def get_nodes(self)->list:
        return self._nodes

    def get_edges(self)->list:
        return self._edges