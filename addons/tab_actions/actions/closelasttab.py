"""This module contains the CloseLastTab proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class CloseLastTab(ActionProxy):
    def __init__(self):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="775wVW80X0u_jcJi9jfJxw",
            classname="CloseLastTab"
        )
