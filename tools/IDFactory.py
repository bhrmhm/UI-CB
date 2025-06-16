import uuid
class IDFactory:
    """ Factory class to be able to get random ID in our system"""

    def __init__(self):
        self._id = -1

    def get_new_id(self)->int:
        """ Generate a new ID by incrementing the current ID """
        self._id += 1
        return self._id

    @staticmethod
    def get_random_id()-> str:
        """ Generate a random UUID as a string """
        return str(uuid.uuid4())

    def get_uri_id(self, workflow_name: str, node_type: str, node_name: str = "", suffix: bool = True) -> str:
        node_name = node_name or "node"
        base = f"urn:workflow:{self.remove_character(workflow_name)}:{self.remove_character(node_type)}:{self.remove_character(node_name)}"
        if suffix:
            return f"{base}:{str(uuid.uuid4())[:4]}"
        return base

    @staticmethod
    def remove_character(text: str) -> str:
        return text.lower().strip().replace(" ", "-").replace("_", "-")