from src.model.AtomicNode import AtomicNode


class StartProcess(AtomicNode):
    def execute(self) -> None:
        super().execute()

    def to_py(self, indent=0, target_id:str=None) -> str:
        return super().to_py(indent)


    def __init__(self, id_:str, name: str, description: str, code_py: list[str],label:str):
        super().__init__(id_, name, description, code_py,label)
