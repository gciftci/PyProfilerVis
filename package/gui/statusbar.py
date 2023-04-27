# package\gui\statusbar.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStatusBar, QGridLayout, QLabel


class StatusBar(QStatusBar):
    def __init__(self, parent=None, status="Idle"):
        """
        Initialize the status bar widget.

        Args:
            parent (QWidget, optional): The parent widget for the status bar. Defaults to None.
            status (str, optional): The initial status text. Defaults to "Idle".
        """
        super(StatusBar, self).__init__(parent)
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.text = QLabel(status)
        self.layout.addWidget(self.text, 0, 0, alignment=Qt.AlignLeft)
        ''' @TODO
            - Add a create_widget method to add things to the statusbar
            - Add some useful info (maybe hover?)
        '''
    def update_status(self, new_status: str):
        """
        Update the status text displayed in the status bar.

        Args:
            new_status (str): The new status text to display.
        """
        self.text.setText(new_status)
