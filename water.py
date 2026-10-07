import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
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
        self.movie = QMovie("avatar2.gif")
        self.anim_label.setMovie(self.movie)
        self.movie.start()
        layout.addWidget(self.anim_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create custom buttons
        btn_layout = QHBoxLayout()
        btn_continue = QPushButton("Continue")
        btn_close = QPushButton("Close")
        
        # Button actions
        btn_continue.clicked.connect(self.on_continue)
        btn_close.clicked.connect(self.close)
        
        btn_layout.addWidget(btn_continue)
        btn_layout.addWidget(btn_close)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def on_continue(self):
        print("Continue action triggered")
        # Add logic for what happens when continue is clicked
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnimationOverlay()
    window.show()
    sys.exit(app.exec())
