from src.models.nodes import AVLNode


class ImbalancedException(ValueError):

    def __init__(self, node: AVLNode, balance: int):
        super().__init__(
            f"Balance condition violated at node: {node} with balance: {balance}"
        )
