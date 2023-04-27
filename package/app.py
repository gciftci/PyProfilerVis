# package\app.py
import sys
from rich.traceback import install
from PyQt5.QtWidgets import QApplication

from package.gui.main_window import Window


def run():
    # Rich Traceback
    install(show_locals=True)

    # headers, data, progress_total_time = process_data(input_str, regex, header)
    # headers, data, progress_total_time = Utils.process_data()

    PyProfilerVis = QApplication(sys.argv)
    PyProfilerVis.setObjectName("PyProfilerVis")
    PyProfilerVis.setApplicationDisplayName("PyProfilerVis")

    PyProfilerVis_UI = Window()
    PyProfilerVis_UI.show()
    try:
        sys.exit(PyProfilerVis.exec_())
    except Exception as e:
        import traceback
        print("Unhandled exception occurred:", e)
        print("Traceback:")
        print(traceback.format_exc())
