"""This module contains the NewTabAtURL proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class NewTabAtURL(ActionProxy):
    def __init__(self, URL: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="775wVW80X0u_jcJi9jfJxw",
            classname="NewTabAtURL"
        )
        self.URL = URL
