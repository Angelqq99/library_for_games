from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel,QComboBox,QSizePolicy,QCheckBox,QGridLayout
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtGui import QPixmap
import sys
#hello
class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('WikiOfGames')
        #self.resize(QSize(500, 500))
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget,spacing = 0)
        #self.layout.addStretch(1)
        
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
        new_layout = QGridLayout(new_widget)
        new_layout.setContentsMargins(0, 0, 0, 0)
        new_layout.setSpacing(0)
        games = ['1', '2', '3', '4']
        
        row = 0  
        for option in games:
            option_button = QPushButton(option, new_widget)
            option_button.clicked.connect(self.characters_window)
            new_layout.addWidget(option_button, row, 0, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            row += 1 

        back_button = QPushButton('Back', new_widget)
        close_button = QPushButton('Close', new_widget)
        close_button.clicked.connect(self.close)
        back_button.clicked.connect(self.go_back)
        
        new_layout.addWidget(back_button)
        row += 1
        new_layout.addWidget(close_button)
        
        self.setCentralWidget(new_widget)

    def characters_window(self):
        characters_widget = QWidget()
        self.setCentralWidget(characters_widget)
        
        characters_layout = QGridLayout(characters_widget)
        characters_layout.setContentsMargins(0, 0, 0, 0)
        characters_layout.setSpacing(0)
        
        characters = ['char1','char2','char3','char4']
    
        for option in characters:
            option_button = QPushButton(option, characters_widget)
            option_button.clicked.connect(self.getInfo)
            characters_layout.addWidget(option_button)
            characters_layout.setAlignment(option_button, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
       
        back_button = QPushButton('Back', characters_widget)
        close_button = QPushButton('Close', characters_widget)
        close_button.clicked.connect(self.close) 
        back_button.clicked.connect(self.open_main_window)
        characters_layout.addWidget(back_button)
        characters_layout.addWidget(close_button)
    
    def getInfo(self):
        info_widget = QWidget(self)
        info_layout = QGridLayout(info_widget)
        
        label = QLabel(info_widget)
        pixmap = QPixmap('D:\VS Code\Projects\library_for_games\image.jpg')
        
        label.setPixmap(pixmap)
        info_layout.addWidget(label)
        
        
        text_label = QLabel("Описание персонажа", info_widget)
        info_layout.addWidget(text_label)
        
        back_button = QPushButton("Back", info_widget)
        back_button.clicked.connect(self.characters_window)
        info_layout.addWidget(back_button)
        
        close_button = QPushButton("Close", info_widget)
        close_button.clicked.connect(self.close)
        info_layout.addWidget(close_button)
        
        info_layout.setAlignment(label, Qt.AlignmentFlag.AlignCenter)  
        info_layout.setAlignment(text_label, Qt.AlignmentFlag.AlignCenter)  
        
        
        info_layout.setAlignment(back_button, Qt.AlignmentFlag.AlignRight)
        info_layout.setAlignment(close_button, Qt.AlignmentFlag.AlignRight)
        
        self.setCentralWidget(info_widget)
        #self.resize(pixmap.width(), pixmap.height())

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
        settings_layout = QGridLayout(settings_widget)
        back_button.clicked.connect(self.go_back)
        settings_layout.addWidget(back_button);
        settings_layout.addWidget(resolution_combo)
        self.fullscreen_checkbox = QCheckBox("Полноэкранный режим", settings_widget)
        self.fullscreen_checkbox.setChecked(True)
        self.fullscreen_checkbox.stateChanged.connect(self.toggle_fullscreen)
        settings_layout.addWidget(self.fullscreen_checkbox)  
        settings_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        resolution_combo.currentTextChanged.connect(lambda: self.update_window_size(resolution_combo.currentText(), settings_widget))
        
    def toggle_fullscreen(self, state):
        if state == 2:  
            self.showFullScreen()
        else:
            self.showNormal()
        
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
        self.layout = QGridLayout(self.central_widget)

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
