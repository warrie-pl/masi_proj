import customtkinter as ctk


class DrawingFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=master.winfo_width(), height=master.winfo_height())
        self.label = ctk.CTkLabel(master=self, text='MASI Project')
        self.label.pack(padx=10, pady=10, side=ctk.TOP)


class OptionsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=master.winfo_width()//3, height=master.winfo_height())
        self.pack_propagate(False)
        self.label = ctk.CTkLabel(master=self, text='Uniterm', font=("Quantico", 60))
        self.label.pack(padx=10, pady=20, side=ctk.TOP)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = 'MASI Project'
        self.minsize(1024, 768)
        self.resizable(False, False)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.options_frame = OptionsFrame(master=self)
        self.options_frame.grid(row=0, column=0, rowspan=2, sticky=ctk.NS)
        self.left_drawing_frame = DrawingFrame(master=self)
        self.left_drawing_frame.grid(row=0, column=1, sticky=ctk.NSEW)
        self.right_drawing_frame = DrawingFrame(master=self)
        self.right_drawing_frame.grid(row=0, column=2, sticky=ctk.NSEW)
        self.bottom_drawing_frame = DrawingFrame(master=self)
        self.bottom_drawing_frame.grid(row=1, column=1, columnspan=2, sticky=ctk.NSEW)
        self.testlabel = ctk.CTkLabel(master=self.right_drawing_frame, text="testlabel")
        self.testlabel.pack(padx=10, pady=10, side=ctk.TOP)



def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
