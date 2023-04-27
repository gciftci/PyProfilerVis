# package\gui\table.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QHeaderView, QTableView, QTableWidgetItem, QProgressBar


class Table(QTableWidget):
    def __init__(self, parent=None):
        """
        Initialize the table widget.

        Args:
            parent (QWidget, optional): The parent widget for the table. Defaults to None.
        """
        super(Table, self).__init__(parent)

        # Empty data
        self.data = {}
        self.headers = []
        self.progress_total_time = 0

        # Table-Configuration
        self.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setSelectionMode(QTableView.SingleSelection)
        self.setEditTriggers(QTableView.NoEditTriggers)
        self.setShowGrid(False)

        # Signal: sectionClicked => self.sort_table
        self.horizontalHeader().sectionClicked.connect(self.sort_table)

    def redraw_table(self, headers, data, progress_total_time):
        """
        Redraw the table with new headers, data, and progress total time.

        Args:
            headers (List[str]): A list of
            header strings for each column.
            data (List): A list of tuples, each tuple representing a row of data.
            progress_total_time (int): The total time for progress bars in the table.
        """

        # Clear all Data
        self.clear_table()
        self.headers = headers
        self.data = data
        self.progress_total_time = progress_total_time

        # Create new Col/Rows and change resize Mode
        self.setColumnCount(len(self.headers))
        self.setRowCount(len(self.data))

        # Populate table
        self.insert_table()

        # Fixate Header-Width to min
        self.redraw_col_width()
        self.horizontalHeader().setSectionResizeMode(len(self.headers) - 1, QHeaderView.Stretch)
        self.setHorizontalHeaderLabels(self.headers)

    def clear_table(self):
        while self.rowCount() > 0:
            self.removeRow(0)
        while self.columnCount() > 0:
            self.removeColumn(0)

    def redraw_col_width(self):
        for i, header in enumerate(self.headers[:-1]):
            self.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)
            self.resizeColumnToContents(i)

            # Set the column width for the progress column based on the maximum value of the timeline data
            self.setColumnWidth(-1, self.progress_total_time)
            # Make the Filename column resizable
            self.horizontalHeader().setSectionResizeMode(len(self.headers) - 2, QHeaderView.Interactive)

    def insert_table(self):
        # Insert data into the table
        self.horizontalHeader().setSectionResizeMode(len(self.headers) - 1, QHeaderView.Stretch)
        self.setHorizontalHeaderLabels(self.headers)
        last_post = 0
        for row_idx, row_data in enumerate(self.data):
            for col_idx, cell_data in enumerate(row_data[:-1]):  # Exclude the last column data (Timeline)
                item = QTableWidgetItem(str(cell_data))
                self.setItem(row_idx, col_idx, item)
            if type(row_data[-1]) == int:
                last_post += row_data[-1]
            progress = self.create_progressbar(last_post, row_data[-1], row_idx, row_data)
            self.setCellWidget(row_idx, len(row_data) - 1, progress)

    def create_progressbar(self, last_post, last_entry, row_idx, row_data):
        # Create QProgressBar for the Timeline column
        progress = QProgressBar()
        progress.setStyleSheet(
            "QProgressBar {"
            'background-color : transparent;'
            "border : None;"
            f"margin-left : {last_post};"
            "}")
        print(f"{row_data[-1]} ({type(row_data[-1])}) for {row_idx}")
        progress.setValue(row_data[-1])
        progress.setAlignment(Qt.AlignCenter)
        progress.setFormat("%vms")
        progress.setRange(0, self.progress_total_time)
        # [progress.setTextVisible(True) if last_entry > 0 else progress.setTextVisible(False)]
        return progress

    def sort_table(self, index: int):
        """
        Sort the table by the clicked header index.

        Args:
            index (int): The index of the clicked header.
        """
        self.data.sort(key=lambda x: x[index], reverse=True)
        self.redraw_table(self.headers, self.data, self.progress_total_time)
