"""This module contains the CountAllTabs proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class CountAllTabs(ActionProxy):
    def __init__(self):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="775wVW80X0u_jcJi9jfJxw",
            classname="CountAllTabs"
        )
        self.numOfTabs = None
