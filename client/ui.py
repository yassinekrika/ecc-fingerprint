import customtkinter
from tkinter import filedialog as fd
from PIL import Image
from client import *

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Log in")
        self.add("Sign in")

        # add widgets on tabs
        self.label = customtkinter.CTkLabel(master=self.tab("Log in"), text="username")
        self.label.grid(row=0, column=0, padx=20, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self.tab("Sign in"), text="username")
        self.label2.grid(row=1, column=0, padx=20, pady=10)

        self.entry = customtkinter.CTkEntry(self.label, placeholder_text="username", width=400) 
        self.entry.grid(row=0, column=1, padx=20, pady=10)

        self.button = customtkinter.CTkButton(self.label, width=400, text="Add Fingerprint")
        self.button.grid(row=1, column=1, padx=20, pady=10)

        self.openImg = customtkinter.CTkButton(self.label, width=400, text="Log In")
        self.openImg.grid(row=2, column=1, padx=20, pady=10)

        self.entry = customtkinter.CTkEntry(self.label2, placeholder_text="username", width=400) 
        self.entry.grid(row=0, column=1, padx=20, pady=10)

        self.button = customtkinter.CTkButton(self.label2, width=400, text="Add Fingerprint")
        self.button.grid(row=1, column=1, padx=20, pady=10)

        self.openImg = customtkinter.CTkButton(self.label2, width=400, text="Sign in")
        self.openImg.grid(row=2, column=1, padx=20, pady=10)

        # fingerprint image Label 
        self.my_image = customtkinter.CTkImage(light_image=Image.open("/home/yassg4mer/Project/ecc_finger_print/client/public/elliptic-curve-cryptography-diagram.png"), size=(300, 300))
        self.label_img = customtkinter.CTkLabel(self.label, image=self.my_image, text='')
        self.label_img.grid(row=4, column=1, padx=20, pady=10)

        # fingerprint image Label 2
        self.my_image = customtkinter.CTkImage(light_image=Image.open("/home/yassg4mer/Project/ecc_finger_print/client/public/elliptic-curve-cryptography-diagram.png"), size=(300, 300))
        self.label_img = customtkinter.CTkLabel(self.label2, image=self.my_image, text='')
        self.label_img.grid(row=4, column=1, padx=20, pady=10)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x580")
        self.maxsize(600, 580)
        self.title("TP CRYPTO")

        self.tab_view = MyTabView(master=self, width=560, height=460)
        self.tab_view.grid(padx=20, pady=20)
    
    def fingerPrint():
        pass


app = App()
app.mainloop()
