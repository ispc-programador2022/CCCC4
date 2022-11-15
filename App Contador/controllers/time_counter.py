from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QThread, Signal
from PySide6 import QtWidgets, QtCore

from views.time_counter import ViewTimeCounter
from scrapper import get_time_count


class TimeCounterThrea(QThread):
    send = Signal(str)
    
    def run(self):
        self.running = True
        while self.running:
            counts = get_time_count()
            self.send.emit(counts)
    
    def stop(self):
        self.running = False



class TimeCounterController(QWidget, ViewTimeCounter):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.create_thread()
    
    def create_thread(self):
        self.thread = TimeCounterThrea()
        self.thread.send.connect(self.set_counts)
        self.thread.start()
    
    def closeEvent(self, event):
        self.thread.stop()
        self.thread.wait()
    
    def set_counts(self, counts):
        
        counts = get_time_count()
        
        print(counts)
        self.counts_label.setText(counts)

 