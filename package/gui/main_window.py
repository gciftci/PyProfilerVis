# package\gui\main_window.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from package.gui.toolbar import ToolBar, MenuBar
from package.gui.table import Table
from package.gui.statusbar import StatusBar


class Window(QMainWindow):
    def __init__(self, parent=None):
        """
        A PyQt5 application that displays a table with a progress bar in the last column.

        Args:
            parent (QWidget, optional): The parent widget for the main window. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("cProfile Visualizer")
        self.resize(1200, 800)
        self.setMinimumSize(1200, 800)

        # Create Table
        self.table = Table(self)

        # Create Toolbar, Menubar and Statusbar
        self.toolbar = ToolBar(self)
        self.menubar = MenuBar(self)
        self.statusbar = StatusBar(self)
        self.wrap_content()

    def wrap_content(self):
        """
        Set the main window's central widget, toolbar, and menubar.
        """
        # Add Table as CentralWidget
        self.setCentralWidget(self.table)
        # Add Top-Bar
        self.addToolBar(self.toolbar)
        self.setMenuBar(self.menubar)
        self.setStatusBar(self.statusbar)
