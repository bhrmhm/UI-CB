from src.model.AtomicNode import AtomicNode


class EndProcess(AtomicNode):
    def execute(self) -> None:
        super().execute()

    def to_py(self, indent=0, target_id:str=None) -> str:
        super().to_py(indent, target_id)
        indent = "    " * indent
        return indent+self._code_py[0]


    def __init__(self,id_:str, name: str, description: str, code_py: list[str],label:str):
        super().__init__(id_,name, description, code_py,label)