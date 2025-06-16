from src.model.Task import Task


class AtomicNode(Task):

    def execute(self) -> None:
        pass

    def to_py(self, indent: int = 0,target_id:int=None) -> str:
        return super().to_py(indent,target_id)

    def __init__(self,id_:str, name: str, description: str, code_py: list[str],label:str):
        super().__init__(id_,name, description, code_py,label)