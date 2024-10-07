from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel,QComboBox
from PyQt6.QtCore import QSize,Qt
import sys

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('WikiOfGames')
        #self.resize(QSize(500, 500))
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        
        self.start_button = QPushButton('Start', self)
        self.settings_button = QPushButton('Settings',self)
        self.start_button.clicked.connect(self.open_main_window)
        self.settings_button.clicked.connect(self.open_settings_window)
        
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.settings_button)
        self.layout.setAlignment(self.start_button,Qt.AlignmentFlag.AlignCenter)
        self.layout.setAlignment(self.settings_button,Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        
    def open_main_window(self):
        new_widget = QWidget()
        new_layout = QVBoxLayout(new_widget)
        new_layout.setContentsMargins(0, 0, 0, 0)
        new_layout.setSpacing(0)
        
        games = ['1','2','3','4']
    
        for option in games:
            option_button = QPushButton(option, new_widget)
            option_button.clicked.connect(self.characters_window) 
            new_layout.addWidget(option_button)
            new_layout.setAlignment(option_button, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
        close_button = QPushButton('Close', new_widget)
        back_button = QPushButton('Back', new_widget)
        back_button.clicked.connect(self.go_back)
        close_button.clicked.connect(self.close) 
        new_layout.addWidget(close_button)
        new_layout.addWidget(back_button)
    
        self.setCentralWidget(new_widget)
    def characters_window(self):
        characters_widget = QWidget()
        self.setCentralWidget(characters_widget)
        
        characters_layout = QVBoxLayout(characters_widget)
        characters_layout.setContentsMargins(0, 0, 0, 0)
        characters_layout.setSpacing(0)
        
        games = ['char1','char2','char3','char4']
    
        for option in games:
            option_button = QPushButton(option, characters_widget)
            characters_layout.addWidget(option_button)
            characters_layout.setAlignment(option_button, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
    def open_settings_window(self):
        settings_widget = QWidget()
        self.setCentralWidget(settings_widget)
        resolution_combo = QComboBox()
        back_button = QPushButton('Back',settings_widget)
        resolution_combo.addItems(['1920*1080', '1280*1024'])  
        settings_layout = QVBoxLayout(settings_widget)
        back_button.clicked.connect(self.go_back)
        settings_layout.addWidget(back_button);
        settings_layout.addWidget(resolution_combo)
        settings_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        resolution_combo.currentTextChanged.connect(lambda: self.update_window_size(resolution_combo.currentText(), settings_widget))
    def update_window_size(self,current_resolution,settings_widget):
        match current_resolution:
            case '1920*1080':
                self.resize(QSize(1920, 1080))
            case '1280*1024':
                self.resize(QSize(500,200))
    def go_back(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.start_button = QPushButton('Start', self)
        self.settings_button = QPushButton('Settings', self)
        
        self.start_button.clicked.connect(self.open_main_window)
        self.settings_button.clicked.connect(self.open_settings_window)

        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.settings_button)
        self.layout.setAlignment(self.settings_button, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        
        
        
app = QApplication(sys.argv)

start_window = StartWindow()
start_window.showFullScreen()
start_window.show()

app.exec()
