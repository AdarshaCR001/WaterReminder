import tkinter as tk

class WaterReminder:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True) # Remove window borders
        self.root.attributes('-topmost', True) # Keep on top
        
        # macOS transparency magic: makes the window background completely invisible
        self.root.wm_attributes('-transparent', True)
        self.root.config(bg='systemTransparent')

        # Load animated GIF frames
        self.frames = []
        try:
            i = 0
            while True:
                # Replace 'avatar.gif' with your actual animated GIF file name
                frame = tk.PhotoImage(file='avatar.gif', format=f'gif -index {i}')
                self.frames.append(frame)
                i += 1
        except tk.TclError:
            pass # Reached the last frame of the GIF

        # Text Bubble
        self.msg_label = tk.Label(root, text="Don't make me come over there.\nDrink water.", 
                                  font=("Arial", 14, "bold"), bg="#2d2d2d", fg="white", 
                                  padx=15, pady=10, relief="flat")
        self.msg_label.pack(pady=(0, 10))

        # Animated Character
        self.char_label = tk.Label(root, bg='systemTransparent')
        self.char_label.pack()

        # Buttons (Dark theme matching your screenshot)
        self.btn_frame = tk.Frame(root, bg='systemTransparent')
        self.btn_frame.pack(pady=10)

        self.btn_drink = tk.Button(self.btn_frame, text="Drink ✅", command=self.close_app, 
                                   bg="#333333", fg="white", highlightbackground="#333333")
        self.btn_drink.pack(side=tk.LEFT, padx=5)

        self.btn_snooze = tk.Button(self.btn_frame, text="Snooze 10m", command=self.close_app, 
                                    bg="#333333", fg="white", highlightbackground="#333333")
        self.btn_snooze.pack(side=tk.LEFT, padx=5)

        # Position window on screen
        self.center_window(350, 400)
        
        # Start animation
        self.frame_index = 0
        self.animate_gif()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def animate_gif(self):
        if self.frames:
            # Cycle through frames
            frame = self.frames[self.frame_index]
            self.char_label.config(image=frame)
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            
            # Schedule next frame (e.g., 100ms for 10fps)
            self.root.after(100, self.animate_gif)

    def close_app(self):
        # Here you could load a "walking away" GIF before destroying
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterReminder(root)
    root.mainloop()
