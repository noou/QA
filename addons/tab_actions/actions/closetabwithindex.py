"""This module contains the CloseTabWithIndex proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class CloseTabWithIndex(ActionProxy):
    def __init__(self, TabIndex: int):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="775wVW80X0u_jcJi9jfJxw",
            classname="CloseTabWithIndex"
        )
        self.TabIndex = TabIndex
