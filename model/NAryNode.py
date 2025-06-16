from src.model.Task import Task


class NAryTask(Task):
    def __init__(self,id_:str, name: str, description: str, code_py: list[str],label:str):
        """
        Two pairing N-ary tasks have the same label
        param :
        last_node : last node of the N-ary task, if None, it means it is already the last_node"""
        super().__init__(id_,name, description, code_py,label)
        self._last_node:Task = None

    def set_last_node(self,last_node:Task,last_node_label:str):
        if not last_node_label == self._label:
            raise RuntimeError(f"Last node label : {last_node_label} doesn't match node label : {self._label}")
        self._last_node = last_node

    def execute(self) -> None:
        pass

    def to_py(self, indent: int = 0, target_id:str=None) -> str:
        if self._label == target_id:
            return ""
        code = ""
        # first we reach the successors
        for successor_code in self._successors:
            if self._last_node is not None:  # means we're in the first node
                code += f"{successor_code.to_py(indent, self._last_node.get_label())}\n"  # we put the target_id in the last node so we don't go any further
            else:
                code += f"{successor_code.to_py(indent, target_id)}\n"  # we're in the last node

        if self._last_node is not None:
            code += self._last_node.to_py(indent, target_id)

        return code




