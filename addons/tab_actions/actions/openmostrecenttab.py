"""This module contains the OpenMostRecentTab proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class OpenMostRecentTab(ActionProxy):
    def __init__(self):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="775wVW80X0u_jcJi9jfJxw",
            classname="OpenMostRecentTab"
        )
