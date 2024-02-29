from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import ImageTk, Image
from database import Database
from customMessageBox import CustomMessageBox

db = Database()
ID = None


class FrameLogin(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller
        self.configure(fg_color="#7b9f9c")

        # self.grid(row=0, column=0, padx=25, pady=25, sticky="nsew")
        self.create_login_segment().grid(row=0, column=0, padx=(30, 25), pady=20)
        self.create_signup_with_image().grid(row=0, column=1, padx=(0, 30), pady=20)

    def create_login_segment(self):
        login_frame = customtkinter.CTkFrame(master=self)

        us_label = customtkinter.CTkLabel(master=login_frame,
                                          text="Username : ",
                                          text_color="#384c3f",
                                          fg_color="transparent",
                                          font=("Impact", 30, "normal"), )

        self.user_input_email = customtkinter.CTkEntry(master=login_frame,
                                                       width=200,
                                                       height=40,
                                                       corner_radius=10,
                                                       placeholder_text="name",
                                                       border_width=0)

        ps_label = customtkinter.CTkLabel(master=login_frame,
                                          text="Password : ",
                                          text_color="#384c3f",
                                          fg_color="transparent",
                                          font=("Impact", 30, "normal"))

        self.user_input_ps = customtkinter.CTkEntry(master=login_frame,
                                                    height=40,
                                                    width=200,
                                                    corner_radius=10,
                                                    border_width=0,
                                                    placeholder_text="********")

        login_btn = customtkinter.CTkButton(master=login_frame,
                                            text="Login",
                                            font=("Impact", 30, "normal"),
                                            height=50,
                                            fg_color="#1e1f34",
                                            hover_color="#4c4e73",
                                            command=lambda: self.log_func())

        us_label.grid(row=0, column=0, padx=20, pady=20)
        self.user_input_email.grid(row=1, column=0, padx=20)
        ps_label.grid(row=2, column=0, padx=20, pady=20)
        self.user_input_ps.grid(row=3, column=0, padx=20)
        login_btn.grid(row=4, column=0, padx=20, pady=20)

        return login_frame

    def create_signup_with_image(self):
        signup_frame = customtkinter.CTkFrame(master=self, fg_color="#7b9f9c")

        global img
        img = ImageTk.PhotoImage(Image.open("src/locker.jpeg").resize((180, 180)))
        locker_image_label = Label(master=signup_frame,
                                   image=img,
                                   border=0)

        sign_up_btn = customtkinter.CTkButton(master=signup_frame,
                                              text="Sign up",
                                              font=("Impact", 30, "normal"),
                                              height=50,
                                              fg_color="#a3c1b8",
                                              text_color="#384c3f",
                                              hover_color="#c5e1d2",
                                              command=lambda: self.controller.show_frame(FrameSignUp))

        locker_image_label.grid(row=0, column=1, pady=30, padx=20)
        sign_up_btn.grid(row=1, column=1, padx=20, pady=15)

        return signup_frame

    def log_func(self):
        global ID
        pw_ = self.user_input_ps.get()
        em_ = self.user_input_email.get()

        user_data = db.sign_in_and_verify(email=em_, password=pw_)
        if user_data:
            ID = user_data['localId']
            self.controller.show_frame(FrameHomePage)


class FrameSignUp(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller
        self.configure(fg_color="#7b9f9c")

        # self.grid(row=0, column=0, padx=25, pady=25, sticky="nsew")
        self.create_signup_segment().grid(row=0, column=0, padx=30, pady=20, sticky="nsew")
        self.img_frame().grid(row=0, column=1, padx=(0, 25), pady=20, sticky="nsew")

    def create_signup_segment(self):
        signup_frame = customtkinter.CTkFrame(master=self)

        us_label = customtkinter.CTkLabel(master=signup_frame,
                                          text="Email : ",
                                          text_color="#384c3f",
                                          fg_color="transparent",
                                          font=("Impact", 30, "normal"), )

        self.user_input_name = customtkinter.CTkEntry(master=signup_frame,
                                                      width=200,
                                                      height=40,
                                                      corner_radius=10,
                                                      placeholder_text="name",
                                                      border_width=0)

        ps_label = customtkinter.CTkLabel(master=signup_frame,
                                          text="Password : ",
                                          text_color="#384c3f",
                                          fg_color="transparent",
                                          font=("Impact", 30, "normal"))

        self.user_input_ps = customtkinter.CTkEntry(master=signup_frame,
                                                    height=40,
                                                    width=200,
                                                    corner_radius=10,
                                                    border_width=0,
                                                    placeholder_text="********")

        confirm_ps_label = customtkinter.CTkLabel(master=signup_frame,
                                                  text="Confirm Password : ",
                                                  text_color="#384c3f",
                                                  fg_color="transparent",
                                                  font=("Impact", 30, "normal"))

        self.confirm_user_input_ps = customtkinter.CTkEntry(master=signup_frame,
                                                            height=40,
                                                            width=200,
                                                            corner_radius=10,
                                                            border_width=0,
                                                            placeholder_text="********")

        sign_btn = customtkinter.CTkButton(master=signup_frame,
                                           text="Sign up",
                                           font=("Impact", 30, "normal"),
                                           height=50,
                                           fg_color="#1e1f34",
                                           hover_color="#4c4e73",
                                           command=lambda: self.sign_func())

        us_label.grid(row=0, column=0, padx=20, pady=20)
        self.user_input_name.grid(row=1, column=0, padx=20)
        ps_label.grid(row=2, column=0, padx=20, pady=20)
        self.user_input_ps.grid(row=3, column=0, padx=20)
        confirm_ps_label.grid(row=4, column=0, padx=20, pady=20)
        self.confirm_user_input_ps.grid(row=5, column=0, padx=20, pady=10)
        sign_btn.grid(row=6, column=0, padx=20, pady=20)

        return signup_frame

    def img_frame(self):
        img_gen_frame = customtkinter.CTkFrame(master=self)
        img_gen_frame.configure(fg_color="#7b9f9c")
        # img_gen_frame.configure(fg_color="white")

        global img_lock_screen
        img_lock_screen = ImageTk.PhotoImage(Image.open("src/download.png").resize((250, 250)))

        img_lock_screen_label = Label(master=img_gen_frame,
                                      image=img_lock_screen,
                                      border=0,
                                      background="#7b9f9c")

        global return_arrow_img
        # return_arrow_img = ImageTk.PhotoImage(Image.open("src/arrow_h.png").resize((100, 100)))
        return_arrow_img = customtkinter.CTkImage(light_image=Image.open("src/arrow_h.png"),
                                                  dark_image=Image.open("src/arrow_h.png"),
                                                  size=(100, 100))

        back_btn = customtkinter.CTkButton(master=img_gen_frame,
                                           text="",
                                           border_width=0,
                                           hover=False,
                                           fg_color="transparent",
                                           image=return_arrow_img,
                                           command=lambda: self.controller.show_frame(FrameLogin))

        # img_label.grid(row=0, column=0, pady=30, padx=20)
        img_lock_screen_label.grid(row=0, column=0, pady=20)
        back_btn.grid(row=1, column=0, pady=30)

        return img_gen_frame

    def sign_func(self):
        em = self.user_input_name.get()
        pw = self.user_input_ps.get()
        cpw = self.confirm_user_input_ps.get()

        if len(pw) < 6:
            msg_box = CustomMessageBox(msg="Warning", pop_up_text="Password is required to have more than 6 characters")
            msg_box.call_window()
        elif pw != cpw:
            msg_box = CustomMessageBox(msg="Warning", pop_up_text="Passwords doesn't match")
            msg_box.call_window()
        else:
            db.add_user_and_make_db_entry(email=em, password=pw)
            self.controller.show_frame(FrameLogin)


class FrameHomePage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller
        # self.TreeView = None
        self.configure(fg_color="#7b9f9c")

        # self.grid(padx=25, pady=25, sticky="nsew")
        self.generate_tree_view_frame().grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.data_add_remove_view_frame().grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.generate_btn()

    def generate_tree_view_frame(self):
        tree_frame = customtkinter.CTkFrame(master=self)
        self.TreeView = TreeView(parent=tree_frame)
        self.TreeView.bind("<<TreeviewSelect>>", self.update_entry_boxes)
        self.TreeView.bind("<Expose>", self.TreeView.run)
        # self.TreeView.bind("<Visibility>", self.TreeView.run)
        tree_scroll = customtkinter.CTkScrollbar(tree_frame)
        tree_scroll.configure(command=self.TreeView.yview,
                              fg_color="#c5e1d2")
        self.TreeView.configure(yscrollcommand=tree_scroll.set)
        tree_scroll.pack(side=RIGHT, fill=Y)
        self.TreeView.pack(fill=BOTH, expand=True)
        return tree_frame

    def data_add_remove_view_frame(self):
        data_add_remove_frame = customtkinter.CTkFrame(master=self, fg_color="#c5e1d2")

        # create user_Entry_label
        entry_label = customtkinter.CTkLabel(master=data_add_remove_frame,
                                             text="Entry : ",
                                             text_color="#384c3f",
                                             fg_color="transparent",
                                             font=("Impact", 30, "normal"), )

        # Entry_input
        self.user_input_entry = customtkinter.CTkEntry(master=data_add_remove_frame,
                                                       width=200,
                                                       height=40,
                                                       corner_radius=10,
                                                       placeholder_text="site or reference",
                                                       border_width=0)

        # create user_name_label
        us_label = customtkinter.CTkLabel(master=data_add_remove_frame,
                                          text="Username : ",
                                          text_color="#384c3f",
                                          fg_color="transparent",
                                          font=("Impact", 30, "normal"), )

        # username text_input
        self.user_input_name = customtkinter.CTkEntry(master=data_add_remove_frame,
                                                      width=200,
                                                      height=40,
                                                      corner_radius=10,
                                                      placeholder_text="name",
                                                      border_width=0)

        # create user_name_label
        ps_label = customtkinter.CTkLabel(master=data_add_remove_frame,
                                          text="Password : ",
                                          text_color="#384c3f",
                                          fg_color="transparent",
                                          font=("Impact", 30, "normal"), )

        # password text_input
        self.user_input_ps = customtkinter.CTkEntry(master=data_add_remove_frame,
                                                    height=40,
                                                    width=200,
                                                    corner_radius=10,
                                                    border_width=0,
                                                    placeholder_text="********")

        entry_label.grid(row=0, column=0, padx=20, pady=20)
        self.user_input_entry.grid(row=1, column=0, padx=20)
        us_label.grid(row=2, column=0, padx=20, pady=20)
        self.user_input_name.grid(row=3, column=0, padx=20)
        ps_label.grid(row=4, column=0, padx=20, pady=20)
        self.user_input_ps.grid(row=5, column=0, padx=20, pady=(0, 40))

        return data_add_remove_frame

    def generate_btn(self):
        # add_button
        add_btn = customtkinter.CTkButton(master=self,
                                          text="New Entry",
                                          font=("Impact", 25, "normal"),
                                          height=40,
                                          fg_color="#1e1f34",
                                          hover_color="#4c4e73",
                                          command=lambda: [self.TreeView.add_record(
                                              _entry=self.user_input_entry.get(),
                                              username=self.user_input_name.get(),
                                              psw=self.user_input_ps.get()), self.clear_entry_boxes()])

        # update_button
        update_btn = customtkinter.CTkButton(master=self,
                                             text="Update",
                                             font=("Impact", 25, "normal"),
                                             height=40,
                                             fg_color="#1e1f34",
                                             hover_color="#4c4e73",
                                             command=lambda: [self.TreeView.update_record(
                                                 entry=self.user_input_entry.get(),
                                                 username=self.user_input_name.get(),
                                                 psw=self.user_input_ps.get()),
                                                 self.clear_entry_boxes()])

        # delete_button
        delete_btn = customtkinter.CTkButton(master=self,
                                             text="Delete",
                                             font=("Impact", 25, "normal"),
                                             height=40,
                                             fg_color="#1e1f34",
                                             hover_color="#4c4e73",
                                             command=lambda: self.TreeView.delete_selected_records())

        # delete_button
        delete_all_btn = customtkinter.CTkButton(master=self,
                                                 text="Delete All",
                                                 font=("Impact", 25, "normal"),
                                                 height=40,
                                                 fg_color="#1e1f34",
                                                 hover_color="#4c4e73",
                                                 command=lambda: self.TreeView.delete_all_records())

        add_btn.grid(row=1, column=0, padx=20, pady=20)
        update_btn.grid(row=2, column=0, padx=20, pady=(0, 20))
        delete_btn.grid(row=1, column=1, padx=20, pady=20)
        delete_all_btn.grid(row=2, column=1, padx=20, pady=(0, 20))

    def clear_entry_boxes(self):
        self.user_input_entry.delete(0, END)
        self.user_input_name.delete(0, END)
        self.user_input_ps.delete(0, END)

    def update_entry_boxes(self, event):
        self.clear_entry_boxes()
        selected = self.TreeView.focus()

        entry, uname, upw = self.TreeView.item(selected, 'values')
        self.user_input_entry.insert(0, entry)
        self.user_input_name.insert(0, uname)
        self.user_input_ps.insert(0, upw)


class TreeView(ttk.Treeview):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.style = ttk.Style()
        self.style.theme_use("default")

        self.style.configure("Treeview",
                             rowheight=25,
                             borderwidth=0)
        self.style.configure("Treeview.Heading",
                             font=("Impact", 12, 'italic'),
                             background="#5a7b6e",
                             border=0,
                             )

        self.style.map("Treeview",
                       background=[('selected', '#fdfe7f')],
                       foreground=[('selected', '#384c3f')])

        self.count = 0

        self['columns'] = ("Entry", "Username", "Password")

        self.column('#0', width=0, stretch=NO)
        self.column('Entry', anchor=CENTER, width=100)
        self.column('Username', anchor=CENTER, width=100)
        self.column('Password', anchor=CENTER, width=100)

        self.heading('#0', text='', anchor=CENTER)
        self.heading('Entry', text='Entry', anchor=CENTER)
        self.heading('Username', text='Username', anchor=CENTER)
        self.heading('Password', text='Password', anchor=CENTER)

        self.tag_configure('even_row', font=("Impact", 10), background="#a3c1b8", foreground="#384c3f")
        self.tag_configure('odd_row', font=("Impact", 10), background="#ddadad", foreground="#384c3f")

    def clear_all_rec_treeview(self):
        for item in self.get_children():
            self.delete(item)

    def run(self, event):
        self.update_tree()

    def update_tree(self):
        try:
            self.clear_all_rec_treeview()
            result_ = db.return_user_db_data(user_id=ID)
            for instance in result_.each():
                item = instance.val()
                if item is None or instance.key() == 0:
                    continue
                # if int(instance.key()) % 2 == 0:
                self.insert(parent='', index='end', iid=f"{instance.key()}",
                            values=(item['Entry'], item['Username'], item['pass_word']),
                            tags=("even_row",))
        except:
            pass

    def add_record(self, _entry: str, username: str, psw: str):
        if len(username) > 0 and len(psw) > 0 and len(_entry) > 0:
            if self.check_for_multiple_instance(username_=username, pswd_=psw, entry_=_entry):
                msg_box = CustomMessageBox(msg="Warning", pop_up_text="Already exists")
                msg_box.call_window()
            else:
                db.add_new_entry(entry=_entry, username=username, password=psw, user_id=ID)
                self.update_tree()
        else:
            msg_box = CustomMessageBox(msg="Warning", pop_up_text="Please fill all fields")
            msg_box.call_window()

    def delete_all_records(self):
        db.delete_all_entry(user_id=ID)
        self.update_tree()

    def delete_selected_records(self):
        # global ID
        item_ = self.selection()
        for _ in item_:
            db.delete_selected_entry(id_=_, user_id=ID)
        self.update_tree()

    def update_record(self, entry: str, username: str, psw: str):
        # global ID
        selected = self.focus()
        db.update_data_entry(id_=selected, entry_=entry, uname=username, pw=psw, user_id=ID)
        self.update_tree()
        # print(selected) you need the id to access firebase database
        # self.item(selected, values=(entry, username, psw))

    def check_for_multiple_instance(self, entry_, username_, pswd_):
        iter_row_items = [self.item(item_)["values"] for item_ in self.get_children()]
        for item in iter_row_items:
            if item[1] == username_ and str(item[2]) == pswd_ and item[0] == entry_:
                return True


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize main window
        self.resizable(width=False, height=False)
        # self.configure(fg_color="#5a7b6e")
        # self.geometry("600x600")
        self.title("Password Manager")
        self.iconbitmap("src/lock-padlock.ico")

        container = Frame(self, background="#5a7b6e")
        container.pack(side="top", fill="both", expand=True)

        # Taking all the frames in to a dictionary initializing them
        self.frames = {}

        for F in (FrameLogin, FrameSignUp, FrameHomePage):
            frame = F(parent=container, controller=self)

            self.frames[F] = frame

        self.show_frame(FrameLogin)

    def forget_all(self):
        for frm in self.frames.values():
            frm.grid_forget()

    def show_frame(self, cont):
        self.forget_all()
        frame = self.frames[cont]
        frame.grid(row=0, column=0, padx=25, pady=25, sticky="nsew")
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
