from .actions import CloseAllTabs, CloseLastTab, CloseTabWithIndex, CountAllTabs, NewTabAtURL, OpenMostRecentTab


class TabActions:
    @staticmethod
    def closealltabs() -> CloseAllTabs:
        """Close all tabs until only starting tab is remaining."""
        return CloseAllTabs()

    @staticmethod
    def closelasttab() -> CloseLastTab:
        """Close the last tab opened in the browser."""
        return CloseLastTab()

    @staticmethod
    def closetabwithindex(TabIndex: int) -> CloseTabWithIndex:
        """Close the tab at provided index."""
        return CloseTabWithIndex(TabIndex)

    @staticmethod
    def countalltabs() -> CountAllTabs:
        """Count all currently open tabs."""
        return CountAllTabs()

    @staticmethod
    def newtabaturl(URL: str) -> NewTabAtURL:
        """Open a URL in a new tab."""
        return NewTabAtURL(URL)

    @staticmethod
    def openmostrecenttab() -> OpenMostRecentTab:
        """This action switches to the most recent tab opened."""
        return OpenMostRecentTab()
