import customtkinter
from tkinter import filedialog as fd
from PIL import Image
from fignerprint import *
from client import client
from client import verify

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x200")

        self.label = customtkinter.CTkLabel(self, text="User Fingerprint Entered Successfully!!!")
        self.label.pack(padx=20, pady=20)

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.vector = None
        self.toplevel_window = None

        # create tabs
        self.add("Log in")
        self.add("Sign in")

        # add widgets on tabs
        self.label = customtkinter.CTkLabel(master=self.tab("Log in"), text="username")
        self.label.grid(row=0, column=0, padx=20, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self.tab("Sign in"), text="username")
        self.label2.grid(row=1, column=0, padx=20, pady=10)

        self.entry1 = customtkinter.CTkEntry(self.label, placeholder_text="username", width=400) 
        self.entry1.grid(row=0, column=1, padx=20, pady=10)

        self.button = customtkinter.CTkButton(self.label, width=400, text="Add Fingerprint", command=self.finger_print)
        self.button.grid(row=1, column=1, padx=20, pady=10)

        self.login = customtkinter.CTkButton(self.label, width=400, text="Log In")
        self.login.grid(row=2, column=1, padx=20, pady=10)

        self.entry2 = customtkinter.CTkEntry(self.label2, placeholder_text="username", width=400) 
        self.entry2.grid(row=0, column=1, padx=20, pady=10)

        self.button = customtkinter.CTkButton(self.label2, width=400, text="Add Fingerprint", command=self.finger_print)
        self.button.grid(row=1, column=1, padx=20, pady=10)

        self.sign = customtkinter.CTkButton(self.label2, width=400, text="Sign in", command=self.post)
        self.sign.grid(row=2, column=1, padx=20, pady=10)

        # fingerprint image Label 
        self.my_image = customtkinter.CTkImage(light_image=Image.open("/home/yassg4mer/Project/ecc_finger_print/client/public/elliptic-curve-cryptography-diagram.png"), size=(300, 300))
        self.label_img = customtkinter.CTkLabel(self.label, image=self.my_image, text='')
        self.label_img.grid(row=4, column=1, padx=20, pady=10)

        # fingerprint image Label 2
        self.my_image = customtkinter.CTkImage(light_image=Image.open("/home/yassg4mer/Project/ecc_finger_print/client/public/elliptic-curve-cryptography-diagram.png"), size=(300, 300))
        self.label_img = customtkinter.CTkLabel(self.label2, image=self.my_image, text='')
        self.label_img.grid(row=4, column=1, padx=20, pady=10)

    def finger_print(self):
        file_path = fd.askopenfilename()
        self.vector = fingerprint(file_path)
        # print(self.vector)
    
    def post(self):
        username = self.entry2.get()
        response = client(self.vector, username)
        self.entry2.delete(0, "end")

        if response.status_code == 200:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()

    def postVerify(self):
        username = self.entry1.get()
        response = verify(self.vector, username)
        self.entry1.delete(0, "end")

        if response.status_code == 200:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()
    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x580")
        self.maxsize(600, 580)
        self.title("TP CRYPTO")

        self.tab_view = MyTabView(master=self, width=560, height=460)
        self.tab_view.grid(padx=20, pady=20)
    
    


app = App()
app.mainloop()

