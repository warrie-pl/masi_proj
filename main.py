import customtkinter as ctk
from tkinter import StringVar, IntVar


class DrawingFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=master.winfo_width(), height=master.winfo_height())
        self.canvas = ctk.CTkCanvas(master=self)
        self.canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)


class OptionsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=master.winfo_width() // 3, height=master.winfo_height())
        self.pack_propagate(False)
        self.label = ctk.CTkLabel(master=self, text='Uniterm', font=("Arial Narrow", 60))
        self.label.pack(padx=10, pady=20, side=ctk.TOP)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('MASI Projekt Temat 10')
        self.minsize(1024, 768)
        self.resizable(False, False)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.sep_value = StringVar(value=",")
        self.seq_value = IntVar(value=0)

        def get_sep_value(canv):
            canv.create_text(200, 100, text=self.sep_value.get(), fill="black", font="Helvetica 14 bold")

        self.options_frame = OptionsFrame(master=self)
        self.options_frame.grid(row=0, column=0, rowspan=2, sticky=ctk.NS)

        self.left_drawing_frame = DrawingFrame(master=self)
        self.left_drawing_frame.grid(row=0, column=1, sticky=ctk.NSEW)
        self.left_drawing_frame.canvas.create_text(200, 20, text="Pierwszy uniterm", fill="black", font="Arial 14 bold")

        self.right_drawing_frame = DrawingFrame(master=self)
        self.right_drawing_frame.grid(row=0, column=2, sticky=ctk.NSEW)
        self.right_drawing_frame.canvas.create_text(200, 20, text="Drugi uniterm", fill="black", font="Arial 14 bold")

        self.bottom_drawing_frame = DrawingFrame(master=self)
        self.bottom_drawing_frame.grid(row=1, column=1, columnspan=2, sticky=ctk.NSEW)
        self.bottom_drawing_frame.canvas.create_text(400, 20, text="Połączone unitermy", fill="black",
                                                     font="Arial 14 bold")

        self.first_param_header = ctk.CTkLabel(master=self.options_frame, text="Pierwszy parametr")
        self.first_param_header.pack()
        self.first_param_input = ctk.CTkTextbox(master=self.options_frame, width=self.winfo_width() // 4, height=20)
        self.first_param_input.pack()

        self.sec_param_header = ctk.CTkLabel(master=self.options_frame, text="Drugi parametr")
        self.sec_param_header.pack()
        self.sec_param_input = ctk.CTkTextbox(master=self.options_frame, width=self.winfo_width() // 4, height=20)
        self.sec_param_input.pack()

        self.sep_frame = ctk.CTkFrame(master=self.options_frame, fg_color="transparent")
        self.sep_frame.pack(pady=10, side=ctk.TOP)

        self.first_sep_choice = ctk.CTkRadioButton(master=self.sep_frame, text=",", variable=self.sep_value,
                                                   command=lambda: get_sep_value(self.left_drawing_frame.canvas),
                                                   value=",", width=55)
        self.first_sep_choice.pack(side=ctk.LEFT, pady=0)
        self.sec_sep_choice = ctk.CTkRadioButton(master=self.sep_frame, text=";", variable=self.sep_value,
                                                 command=lambda: get_sep_value(self.right_drawing_frame.canvas),
                                                 value=";", width=45)
        self.sec_sep_choice.pack(side=ctk.RIGHT)

        self.seq_frame = ctk.CTkFrame(master=self.options_frame, fg_color="transparent")
        self.seq_frame.pack(pady=10, side=ctk.TOP)

        self.first_seq_choice = ctk.CTkRadioButton(master=self.seq_frame, text="sekwencjonowanie", value=0,
                                                   variable=self.seq_value)
        self.first_seq_choice.pack(side=ctk.LEFT, padx=10)
        self.sec_seq_choice = ctk.CTkRadioButton(master=self.seq_frame, text="eliminacja", value=1,
                                                 variable=self.seq_value)
        self.sec_seq_choice.pack(side=ctk.RIGHT)


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
