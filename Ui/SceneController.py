from src.Ui.Arrow import Arrow



class SceneController:
    def __init__(self, scene, nodes:list):
        self._scene = scene
        self._nodes = nodes
        self._first_node= None
        self._second_node = None

    def node_clicked(self, node):
        print("Clicked:", node, "Pos:", node.pos(), "Parent:", node.parentItem())
        if self._first_node is None:
            self._first_node = node
            print("First node clicked")
        else: #second node clicked: draw an arrow
            self._second_node = node
            print("Second node clicked")
            if self._first_node != self._second_node:
                arrow = Arrow(self._first_node, self._second_node)
                self._first_node.add_to_out_arrows(arrow)
                self._second_node.add_to_in_arrows(arrow)
                self.scene.addItem(arrow)
            self._first_node = None

    def get_scene(self):
        return self._scene

    def get_nodes(self)->list:
        return self._nodes