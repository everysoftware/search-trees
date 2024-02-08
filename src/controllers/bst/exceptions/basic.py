class EmptyTreeException(ValueError):

    def __init__(self):
        super().__init__("Tree is empty")


class EmptyNodeException(ValueError):

    def __init__(self):
        super().__init__("Node is empty")
