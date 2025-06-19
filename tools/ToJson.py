import json
from pathlib import Path

from Env import Env
from src.model.ComputationNode import ComputationNode
from src.model.EndProcess import EndProcess
from src.model.ProcessNode import ProcessNode
from src.model.StartProcess import StartProcess
from tools.IDFactory import IDFactory


class ToJson:
    def __init__(self, title:str, authors:str, description:str, nodes:list, arrows:list, nb_params:int):
        """Create a Json file from the interface"""
        self._factory: IDFactory = IDFactory()
        self._title: str = title
        self._authors: str = authors
        self._description: str = description
        self._nodes_list: list = nodes # List of nodes from the interface
        self._arrows_list: list = arrows # List of arrows from the interface
        self._nb_params: int = nb_params # Number of parameters set in interface
        self._nodes:list = []
        self._edges: list = []
        self._parameters: list = []
        self._create_json()

    def _create_json(self):
        self._create_nodes()
        self._create_edges()
        self._create_parameters()
        self._write_json()

    def _create_nodes(self):
        d = []
        for node in self._nodes_list:
            if isinstance(node, ProcessNode):
                self.add_process_node(d, node)
                print("Encountered a process node")
            elif isinstance(node, StartProcess):
                d.append((node.get_id(),{
                    "id": node.get_id(),
                    "name": node.get_name(),
                    "type": "StartProcess",
                    "codePy": node.get_code_py()[0],
                    "description": "Beginning of workflow",
                    "label":""
                }))
                print("Encountered a start process node")
            elif isinstance(node, EndProcess):
                d.append((node.get_id(),{
                    "id": node.get_id(),
                    "name": node.get_name(),
                    "type": "EndProcess",
                    "codePy": node.get_code_py()[0],
                    "description": "End of workflow",
                    "label":""
                }))
                print("Encountered a end process node")
            elif isinstance(node, ComputationNode):
                self.add_computation_node(d, node)
                print("Encountered a computation node")

        self._nodes = d #d is a list for the moment !!!



    def add_process_node(self,d:list ,node:ProcessNode):
        d.append((node.get_id(), {
            "id": node.get_id(),
            "name": node.get_name(),
            "type": "ProcessNode",
            "codePy": node.get_code_py()[0],
            "description": node.get_description(),
            "label": "",
        }))

    def add_computation_node(self,d:list ,node:ComputationNode):
        d.append((node.get_id(), {
            "id": node.get_id(),
            "name": node.get_name(),
            "type": "ComputationNode",
            "codePy": node.get_code_py()[0],
            "description": node.get_description(),
            "label": node.get_label(),
        }))

    def _create_edges(self):
        d = []
        for arrow in self._arrows_list:
            src = arrow.get_start_task()
            dest = arrow.get_end_task()
            d.append({
                "id": arrow.get_id(),
                "src": src.get_id(),
                "dest": dest.get_id(),
                "label": arrow.get_label(),
            })
        self._edges = d
    def _create_parameters(self):
        p=[]
        for i in range(self._nb_params):
            p.append({
                "name": "",
                "type": "",
                "value": ""

            })
        self._parameters = p



    def _write_json(self):
        resource_path = Path(Env.RESSOURCE_PATH + "/CB")
        resource_path.mkdir(parents=True, exist_ok=True)
        filename = resource_path / f"{self._title}_{self._factory.get_random_id()}.json"
        d = {
            "title": self._title,
            "authors": self._authors,
            "description": self._description,
            "nodes": [node[1] for node in self._nodes],
            "edges": self._edges,
            "parameters": self._parameters,
        }
        json.dump(d, open(filename, 'w'), indent=6)