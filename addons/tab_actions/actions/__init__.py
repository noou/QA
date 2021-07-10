"""This package contains all the addon proxy's actions."""
from .closealltabs import CloseAllTabs
from .closelasttab import CloseLastTab
from .closetabwithindex import CloseTabWithIndex
from .countalltabs import CountAllTabs
from .newtabaturl import NewTabAtURL
from .openmostrecenttab import OpenMostRecentTab

__all__ = ["CloseAllTabs", "CloseLastTab", "CloseTabWithIndex",
           "CountAllTabs", "NewTabAtURL", "OpenMostRecentTab"]
