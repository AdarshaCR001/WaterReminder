import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QMovie

class AnimationOverlay(QWidget):
    def __init__(self):
        super().__init__()
        
        # Frameless window, stays on top, and Tool flag hides it from the Dock/Taskbar
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        layout = QVBoxLayout()
        
        # Load and play the animation
        self.anim_label = QLabel()
        self.movie = QMovie("avatar.gif")
        self.anim_label.setMovie(self.movie)
        self.movie.start()
        layout.addWidget(self.anim_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create custom buttons
        # Create custom buttons
        btn_layout = QHBoxLayout()
        btn_now = QPushButton("Drink Now")
        btn_later = QPushButton("Drink Later")
        
        # Apply black background and white text styling
        button_style = """
            QPushButton {
                background-color: black;
                color: white;
                padding: 8px 16px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #333333; /* Slightly lighter on hover */
            }
        """
        btn_now.setStyleSheet(button_style)
        btn_later.setStyleSheet(button_style)

        
        # Button actions
        btn_now.clicked.connect(self.drink_now)
        btn_later.clicked.connect(self.snooze)
        
        btn_layout.addWidget(btn_now)
        btn_layout.addWidget(btn_later)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        # Initialize the snooze timer
        self.snooze_timer = QTimer(self)
        self.snooze_timer.setSingleShot(True)  # Ensures the timer only runs once per click
        self.snooze_timer.timeout.connect(self.wake_up)

    def drink_now(self):
        print("Water drunk! Closing.")
        QApplication.quit()  # This fully terminates the application and removes the Dock icon

    def snooze(self):
        # Hide the window and start the 5-minute timer
        print("Snoozing for 5 minutes...")
        self.hide() 
        # 5 minutes = 5 * 60 seconds * 1000 milliseconds
        self.snooze_timer.start(5 * 60 * 1000)
        
        # If you want to test it quickly without waiting 5 minutes, 
        # comment the line above and uncomment the 5-second timer below:
        # self.snooze_timer.start(5 * 1000)

    def wake_up(self):
        # Show the window again after the timer finishes
        print("Waking up from snooze...")
        self.show()
        self.raise_()           # Brings window to the top of the GUI stack
        self.activateWindow()   # Forces the OS to give it focus

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnimationOverlay()
    window.show()
    window.raise_()             # Ensures it forces its way to the front on first launch
    window.activateWindow()
    sys.exit(app.exec())

