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
        
        self.layout = QVBoxLayout(self.central_widget,spacing = 0)
        self.layout.addStretch(1)
        
        self.start_button = QPushButton('Start', self)
        self.settings_button = QPushButton('Settings',self)
        self.close_button = QPushButton('Exit',self)
        self.close_button.clicked.connect(self.close)
        self.start_button.clicked.connect(self.open_main_window)
        self.settings_button.clicked.connect(self.open_settings_window)
        
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.settings_button)
        self.layout.addWidget(self.close_button)
        self.layout.setAlignment(self.start_button,Qt.AlignmentFlag.AlignCenter)
        self.layout.setAlignment(self.settings_button,Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        self.layout.setAlignment(self.close_button, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        
    def open_main_window(self):
        new_widget = QWidget()
        new_layout = QVBoxLayout(new_widget)
        new_layout.setContentsMargins(0, 0, 0, 0)
        new_layout.setSpacing(0)
        new_layout.addStretch(1)
        
        games = ['1','2','3','4']
    
        for option in games:
            option_button = QPushButton(option, new_widget)
            option_button.clicked.connect(self.characters_window) 
            new_layout.addWidget(option_button)
            new_layout.setAlignment(option_button, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        

        back_button = QPushButton('Back', new_widget)
        close_button = QPushButton('Close', new_widget)
        close_button.clicked.connect(self.close) 
        back_button.clicked.connect(self.go_back)
        new_layout.addWidget(back_button)
        new_layout.addWidget(close_button)
    
        self.setCentralWidget(new_widget)
    def characters_window(self):
        characters_widget = QWidget()
        self.setCentralWidget(characters_widget)
        
        characters_layout = QVBoxLayout(characters_widget)
        characters_layout.setContentsMargins(0, 0, 0, 0)
        characters_layout.setSpacing(0)
        characters_layout.addStretch(1)
        
        characters = ['char1','char2','char3','char4']
    
        for option in characters:
            option_button = QPushButton(option, characters_widget)
            characters_layout.addWidget(option_button)
            characters_layout.setAlignment(option_button, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
       
        back_button = QPushButton('Back', characters_widget)
        close_button = QPushButton('Close', characters_widget)
        close_button.clicked.connect(self.close) 
        back_button.clicked.connect(self.open_main_window)
        characters_layout.addWidget(back_button)
        characters_layout.addWidget(close_button)
        
    def open_settings_window(self):
        settings_widget = QWidget()
        self.setCentralWidget(settings_widget)
        resolution_combo = QComboBox()
        back_button = QPushButton('Back',settings_widget)
        resolutions = ['1920x1080', 
        '1280x1024', 
        '1366x768', 
        '1600x900', 
        '1440x900', 
        '2560x1440', 
        '3840x2160', 
        '1024x768', 
        '800x600']
        resolution_combo.addItems(resolutions)  
        settings_layout = QVBoxLayout(settings_widget)
        back_button.clicked.connect(self.go_back)
        settings_layout.addWidget(back_button);
        settings_layout.addWidget(resolution_combo)
        settings_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        resolution_combo.currentTextChanged.connect(lambda: self.update_window_size(resolution_combo.currentText(), settings_widget))
    def update_window_size(self,current_resolution,settings_widget):
        match current_resolution:
            case '1920x1080':
                self.resize(QSize(1920, 1080))
            case '1280x1024':
                self.resize(QSize(1280, 1024))
            case '1366x768':
                self.resize(QSize(1366, 768))
            case '1600x900':
                self.resize(QSize(1600, 900))
            case '1440x900':
                self.resize(QSize(1440, 900))
            case '2560x1440':
                self.resize(QSize(2560, 1440))
            case '3840x2160':
                self.resize(QSize(3840, 2160))
            case '1024x768':
                self.resize(QSize(1024, 768))
            case '800x600':
                self.resize(QSize(800, 600))
    def go_back(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.start_button = QPushButton('Start', self)
        self.settings_button = QPushButton('Settings', self)
        
        self.start_button.clicked.connect(self.open_main_window)
        self.settings_button.clicked.connect(self.open_settings_window)
        self.close_button = QPushButton('Exit', self.central_widget)
        self.close_button.clicked.connect(self.close) 

        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.settings_button)
        self.layout.addWidget(self.close_button)
        self.layout.setAlignment(self.start_button,Qt.AlignmentFlag.AlignCenter)
        self.layout.setAlignment(self.settings_button, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        self.layout.setAlignment(self.close_button, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        
        
        
app = QApplication(sys.argv)

start_window = StartWindow()
start_window.showFullScreen()
start_window.show()

app.exec()
