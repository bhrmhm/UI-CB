from src.model.NAryNode import NAryTask
from src.model.Task import Task


class QuestionNode(NAryTask):
    def __init__(self,id_:str, name: str, description: str, code_py: list[str],label:str):
        super().__init__(id_, name, description, code_py,label)
        self._true_branch:Task|None = None
        self._false_branch:Task|None = None
        self._while_false_branch:Task|None = None
        self._while_true_branch: Task | None = None



    def execute(self) -> None:
        super().execute()

    def to_py(self, indent: int = 0, target_id:str=None) -> str:
        """ add the if else statement and adapt the indentation
        """
        if target_id is self._id : return ""
        indent_str = "    " * indent
        lines = [""]
        if self._while_false_branch :
            lines.append(f"{indent_str}while not {self._code_py[0]} :")
            false_code = self._while_false_branch.to_py(indent+1,self._id)
            lines.append(false_code)
        if self._while_true_branch :
            lines.append(f"{indent_str}while {self._code_py[0]} :")
            while_code = self._while_true_branch.to_py(indent + 1, self._id)
            lines.append(while_code)
        if self._true_branch:
            lines.append(f"{indent_str}if {self._code_py[0]}:")
            lines.append(f"{indent_str}    #true branch")
            true_code = self._true_branch.to_py(indent + 1,target_id)
            lines.append(true_code)
        if self._false_branch:
            lines.append(f"{indent_str}if not {self._code_py[0]}:")
            lines.append(f"{indent_str}    #false branch")
            false_code = self._false_branch.to_py(indent + 1,target_id)
            lines.append(false_code)
        return "\n".join(lines)

    def set_true_branch(self, true_task: Task) -> None:
        """ Set the true branch of the question node"""
        self._true_branch = true_task
    def set_false_branch(self, false_task: Task) -> None:
        """ Set the false branch of the question node"""
        self._false_branch = false_task

    def set_while_true_branch(self,while_task:Task) -> None:
        """ Set the beginning of the while branch
        if gives the condition to stop the while loop"""
        self._while_true_branch = while_task

    def set_while_false_branch(self,while_task:Task) -> None:
        """ Set the beginning of the while branch
        if gives the condition to stop the while loop"""
        self._while_false_branch = while_task

    def get_true_branch(self) -> Task:
        """ Get the true branch of the question node"""
        return self._true_branch

    def get_false_branch(self) -> Task:
        """ Get the false branch of the question node"""
        return self._false_branch

    def get_while_true_branch(self) -> Task:
        """ Get the beginning of the while branch
        if gives the condition to stop the while loop"""
        return self._while_true_branch

    def get_while_false_branch(self) -> Task:
        """ Get the beginning of the while branch
        if gives the condition to stop the while loop
        """
        return self._while_false_branch