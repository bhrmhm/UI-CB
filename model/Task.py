from __future__ import annotations
from abc import ABC, abstractmethod


class Task(ABC) :
    """ Abstract class to define every task of the system """

    def __init__(self,id_:str,name:str,description:str,code_py:list[str], label:str):
        """ Constructor of the class """
        self._id:str = id_
        self._name:str = name
        self._description:str = description #TODO : change it for explication class later
        self._code_py:list[str] = code_py
        self._successors:list[Task] = []
        self._label:str = label

    @abstractmethod
    def execute(self) -> None:
        """ Execute the task of the current class"""
        pass
    @abstractmethod
    def to_py(self,indent:int = 1,target_id:str=None)->str:
        """ Convert the task to a python code"""
        pass
    def __str__(self)->str:
        return f"{type(self).__name__} : {self._name} ; {self._id}"

    def get_id(self)->str:
        """ Get the id of the task"""
        return self._id
    def get_name(self)->str:
        """ Get the name of the task"""
        return self._name
    def get_description(self)->str:
        """ Get the description of the task"""
        return self._description



    @staticmethod
    def indent(self) -> int:
        """ Return the indent level of the task
        can be -1 0 1"""
        return 0


    def get_successors(self)->list[Task]:
        """ Get the successors of the task"""
        return self._successors

    def add_successor(self,task:Task)->None:
        """ Add a successor to the task"""
        self._successors.append(task)

    def remove_successor(self,task:Task)->None:
        """ Remove a successor to the task"""
        self._successors.remove(task)

    def get_code_py(self) -> list[str]:
        """ Get the code of the task"""
        return self._code_py