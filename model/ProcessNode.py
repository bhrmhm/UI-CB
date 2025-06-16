from src.model.AtomicNode import AtomicNode


class ProcessNode(AtomicNode):

    def to_py(self, indent: int = 1, target_id:str=None) -> str:
        return super().to_py(indent, target_id)

    def __init__(self, id_:str, name: str, description: str, code_py: list[str],label:str):
        super().__init__(id_, name, description, code_py,label)