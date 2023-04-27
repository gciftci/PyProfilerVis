# package\gui\top_bar.py
from typing import Callable
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QToolBar, QAction, QFileDialog, QSizePolicy, QMenuBar
from package.utils.utils import process_data


class ToolBar(QToolBar):
    def __init__(self, parent):
        super(ToolBar, self).__init__(parent)
        self.setIconSize(QSize(32, 32))
        self.actions = {}

        # Left Side
        self.create_tool("import_action", QIcon('res\\icons\\104.png'), "&Import", self.import_data)
        # Spacer
        self.spacer = QWidget()
        self.spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.addWidget(self.spacer)
        # Right Side
        self.create_tool("remove_action", QIcon('res\\icons\\88.png'), "&Add", self.delete_table)

    def create_tool(self, action_name, tool_icon, tool_name, action_func):
        self.actions[action_name] = QAction(tool_icon, tool_name, self)
        self.actions[action_name].triggered.connect(action_func)
        self.addAction(self.actions[action_name])

    def create_importAction(self):
        importAction = QAction(QIcon(":edit-copy.svg"), "&Copy", self)
        importAction.triggered.connect(self.import_content)
        self.addAction(importAction)

    def delete_table(self):
        # Logic for copying content goes here...
        self.parent().table.clear_table()

    def add_button(self, button_name: str = "empty_button",
                   button_text: str = "Empty!",
                   button_align: Callable = Qt.AlignRight,
                   button_func: Callable = lambda: print("Empty!")):
        # Create the Button
        self[button_name] = QPushButton(button_text)
        self[button_name].clicked.connect(button_func)

        # Add widgets to layout and align
        self.toolbar_layout.addWidget(self.buttons[button_name], 0, len(self.buttons), button_align)

    def import_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt);;All Files (*)",
                                                   options=options)
        if file_name:
            with open(file_name, 'r') as file:
                # lines = [line.rstrip('\n') for line in file_content]
                file_content = file.read()
            regex_pstats = r'^.*?(\S+?)\s+?(\S+?)\s+?(\S+?)\s+?(\S+?)\s+?(\S+?)\s+?(\S.*?)$'
            header_pstats = True
            headers, data, progress_total_time = process_data(file_content, regex_pstats, header_pstats)
            self.parent().table.redraw_table(headers, data, progress_total_time)


class MenuBar(QMenuBar):
    def __init__(self, parent):
        super(MenuBar, self).__init__(parent)

        # File menu
        self.file_menu = self.addMenu("&File")

        # - Open action
        self.open_action = QAction("&Open", self)
        self.open_action.triggered.connect(self.parent().toolbar.import_data)
        self.file_menu.addAction(self.open_action)

        # - Exit action
        self.exit_action = QAction("&Exit", self)
        self.exit_action.triggered.connect(self.parent().close)
        self.file_menu.addAction(self.exit_action)

        # Edit menu
        self.edit_menu = self.addMenu("&Edit")

        # - Delete action
        self.delete_action = QAction("&Delete", self)
        self.delete_action.triggered.connect(self.parent().table.clear_table)
        self.edit_menu.addAction(self.delete_action)

        # Help
        self.help_menu = self.addMenu("&?")

        # - Delete action
        self.help_action = QAction("&Help", self)
        self.help_action.triggered.connect(lambda: print("nah"))
        self.help_menu.addAction(self.help_action)
