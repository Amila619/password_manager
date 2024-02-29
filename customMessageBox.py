import customtkinter
import tkinter
from PIL import ImageTk, Image


class CustomMessageBox(customtkinter.CTkToplevel):
    def __init__(self, msg, pop_up_text):
        super().__init__()
        self.configure(fg_color="#5a7b6e")
        self.iconbitmap("src/ic_warning_128_28766.ico")
        self.img = ImageTk.PhotoImage(Image.open("src/warning.png").resize((40, 40)))
        self.title(msg)
        self.pop_up_text = pop_up_text
        self.attributes("-topmost", "true")
        self.grab_set()


    def call_window(self):
        self.pop_up().pack(padx=20, pady=20)


    def pop_up(self):
        widget_frame = customtkinter.CTkFrame(master=self,
                                              fg_color="#c5e1d2")

        label = customtkinter.CTkLabel(master=widget_frame,
                                       text=self.pop_up_text,
                                       text_color="#384c3f",
                                       fg_color="transparent",
                                       font=("Impact", 20, "normal")
                                       )


        locker_image_label = tkinter.Label(master=widget_frame,
                                           image=self.img,
                                           border=0,
                                           background="#c5e1d2")

        btn = customtkinter.CTkButton(master=widget_frame,
                                      text="OK",
                                      font=("Impact", 20, "normal"),
                                      height=20,
                                      fg_color="#1e1f34",
                                      hover_color="#4c4e73",
                                      command=lambda: self.destroy())

        label.pack(padx=20, pady=20)
        locker_image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        btn.pack(padx=20, pady=(40, 20))

        return widget_frame
