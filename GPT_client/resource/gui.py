"""
Create a GUI to display message
"""

from tkinter import *
from default_library.constants import (BOTTOM, TOP, LEFT, RIGHT, BLACK)

class GUI(object):
    def __init__(self) -> None:
        """
        Create a tkinter windown
        Args: 
            None
        Return:"
            None
        """
        self.window = None
    # End init built-in
    

    def start(self) -> None:
        """
        Start GUI and draw window
        Args: 
            None
        Return:"
            None
        """
        self.window = Tk()
        self.draw_window()
        self.window.mainloop()
    # End start function
        
    
    def draw_window(self) -> None:
        """
        Layout of window
        Args:
            None
        Return:
            None
        """
        total_width = 120
        message_width = 104
        btn_width = 8

        window = self.window
        window.title("ChatGPT server")

        frame = Frame(window, width=total_width+20)
        frame.pack()
        
        right_top_frame = Frame(frame)
        right_top_frame.pack(side=TOP)

        message_box = Text(right_top_frame)
        message_box.config(state="disabled")
        message_box.pack(side=LEFT)
        
        right_bottom_frame = Frame(frame)
        right_bottom_frame.pack(side=BOTTOM)

        self.memessage_entry = message_entry = Entry(right_bottom_frame, width=message_width-btn_width)
        message_entry.pack(side=LEFT)

        send_btn = Button(right_bottom_frame, text='Send', width=btn_width)
        send_btn.pack(side=LEFT)
    # End draw_window function
# End GUI class


gui = GUI()


if __name__ == "__main__":
    pass