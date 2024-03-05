"""
Create a GUI to display message
"""

from tkinter import (Frame, Tk, Button, Text, Entry, END)
from default_library.configuration import DataConfiguration
from default_library.constants import (BOTTOM, TOP, LEFT, RIGHT, BLACK)
from resource.socket import cr 


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
    

    def start(self, config: DataConfiguration) -> None:
        """
        Start GUI and draw window
        Args: 
            None
        Return:"
            None
        """
        self.host = config.host_address
        self.port = config.port_number
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
        total_width = 100
        btn_width = 8

        window = self.window
        window.title("ChatGPT server")

        frame = Frame(window, width=total_width)
        frame.pack()
        
        right_top_frame = Frame(frame)
        right_top_frame.pack(side=TOP)

        self.message_box = message_box = Text(right_top_frame, width=total_width)
        message_box.config(state="disabled")
        message_box.pack(side=LEFT)
        
        right_bottom_frame = Frame(frame)
        right_bottom_frame.pack(side=BOTTOM)

        self.message_entry = message_entry = Entry(right_bottom_frame, width=total_width-btn_width)
        message_entry.pack(side=LEFT)

        send_btn = Button(right_bottom_frame, text='Send', command=self.get_message, width=btn_width)
        send_btn.pack(side=LEFT)
    # End draw_window function
        
    
    def get_message(self) -> None:
        """
        get value in message entry and clean it
        Return:
            None
        """
        message = self.message_entry.get()
        self.message_entry.delete(0, len(message))
        self.message_box.config(state='normal')
        self.message_box.insert(END, ("Me: "+ message+"\n"))
        self.message_box.config(state="disabled")
        cr.send(message, self.host, self.port)
    # End get_message function
# End GUI class


gui = GUI()


if __name__ == "__main__":
    pass