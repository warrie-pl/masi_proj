import customtkinter as ctk
from tkinter import StringVar, IntVar, messagebox


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
        self.uniterm_value = IntVar(value=0)
        self.uniterms = {}

        self.options_frame = OptionsFrame(master=self)
        self.options_frame.grid(row=0, column=0, rowspan=2, sticky=ctk.NS)

        self.left_drawing_frame = DrawingFrame(master=self)
        self.left_drawing_frame.grid(row=0, column=1, sticky=ctk.NSEW)
        self.left_drawing_frame.canvas.create_text(200, 20, text="Lewy uniterm", fill="black", font="Arial 14 bold")

        self.right_drawing_frame = DrawingFrame(master=self)
        self.right_drawing_frame.grid(row=0, column=2, sticky=ctk.NSEW)
        self.right_drawing_frame.canvas.create_text(200, 20, text="Prawy uniterm", fill="black", font="Arial 14 bold")

        self.bottom_drawing_frame = DrawingFrame(master=self)
        self.bottom_drawing_frame.grid(row=1, column=1, columnspan=2, sticky=ctk.NSEW)
        self.bottom_drawing_frame.canvas.create_text(400, 20, text="Połączone unitermy", fill="black",
                                                     font="Arial 14 bold")

        self.first_param_header = ctk.CTkLabel(master=self.options_frame, text="Pierwszy parametr")
        self.first_param_header.pack()
        self.first_param_input = ctk.CTkEntry(master=self.options_frame, width=self.winfo_width() // 4, height=20)
        self.first_param_input.pack()

        self.sec_param_header = ctk.CTkLabel(master=self.options_frame, text="Drugi parametr")
        self.sec_param_header.pack()
        self.sec_param_input = ctk.CTkEntry(master=self.options_frame, width=self.winfo_width() // 4, height=20)
        self.sec_param_input.pack()

        self.sep_frame = ctk.CTkFrame(master=self.options_frame, fg_color="transparent")
        self.sep_frame.pack(pady=10, side=ctk.TOP)

        self.first_sep_choice = ctk.CTkRadioButton(master=self.sep_frame, text=",", variable=self.sep_value, value=",",
                                                   width=55)
        self.first_sep_choice.pack(side=ctk.LEFT, pady=0)
        self.sec_sep_choice = ctk.CTkRadioButton(master=self.sep_frame, text=";", variable=self.sep_value, value=";",
                                                 width=45)
        self.sec_sep_choice.pack(side=ctk.RIGHT)

        self.seq_frame = ctk.CTkFrame(master=self.options_frame, fg_color="transparent")
        self.seq_frame.pack(pady=10, side=ctk.TOP)

        self.first_seq_choice = ctk.CTkRadioButton(master=self.seq_frame, text="sekwencjonowanie", value=0,
                                                   variable=self.seq_value)
        self.first_seq_choice.pack(side=ctk.LEFT, padx=10)
        self.sec_seq_choice = ctk.CTkRadioButton(master=self.seq_frame, text="eliminacja", value=1,
                                                 variable=self.seq_value)
        self.sec_seq_choice.pack(side=ctk.RIGHT)

        self.uniterm_frame = ctk.CTkFrame(master=self.options_frame, fg_color="transparent")
        self.uniterm_frame.pack(pady=10, side=ctk.TOP)

        self.first_uniterm = ctk.CTkRadioButton(master=self.uniterm_frame, text="Lewy", variable=self.uniterm_value,
                                                value=0)
        self.first_uniterm.pack(side=ctk.LEFT)
        self.second_uniterm = ctk.CTkRadioButton(master=self.uniterm_frame, text="Prawy", variable=self.uniterm_value,
                                                 value=1, width=35)
        self.second_uniterm.pack(side=ctk.RIGHT)

        def draw_uniterm(canv: ctk.CTkCanvas, uniterm):
            canv.delete("uniterm")
            if self.seq_value.get() == 0:
                text = canv.create_text(200, 200, text=uniterm, fill="black", font="Arial 14 bold", tags="uniterm")
                bbox = canv.bbox(text)
                canv.create_arc(bbox[0] - 20, bbox[1] - 30, bbox[2], bbox[3]+10, start=120, extent=120,
                                style="arc", tags="uniterm")
            elif self.seq_value.get() == 1:
                text = canv.create_text(200, 200, text=uniterm, fill="black", font="Arial 14 bold", tags="uniterm")
                bbox = canv.bbox(text)
                print(bbox)
                canv.create_line((bbox[0] - 10, bbox[1] - 20, bbox[0] - 10, bbox[3]), tags="uniterm")
                canv.create_line((bbox[0] - 30, bbox[1] - 20, bbox[2], bbox[1] - 20), tags="uniterm")
                canv.create_line((bbox[0] - 30, bbox[3], bbox[2], bbox[3]), tags="uniterm")

        def choose_uniterm():
            val = self.uniterm_value.get()
            first_param = self.first_param_input.get()
            separator = self.sep_value.get()
            second_param = self.sec_param_input.get()
            seq_method = self.seq_value.get()
            self.uniterms[val] = [first_param, separator, second_param, seq_method]
            uniterm_text = ""
            print(self.uniterms[val])
            for item in self.uniterms[val][:-1]:
                uniterm_text = uniterm_text + str(item) + "\n"
            if self.uniterms[val][0] == "" or self.uniterms[val][2] == "":
                messagebox.showinfo("Uniterm", "Uniterm wymaga dwóch parametrów!")
            else:
                if val == 0:
                    draw_uniterm(self.left_drawing_frame.canvas, uniterm_text)
                elif val == 1:
                    draw_uniterm(self.right_drawing_frame.canvas, uniterm_text)

        self.add_uniterm = ctk.CTkButton(master=self.options_frame, text="Dodaj uniterm",
                                         command=choose_uniterm)
        self.add_uniterm.pack(pady=10)


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
