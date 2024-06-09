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
        self.uniterm_to_transform = IntVar(value=0)
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

        self.uniterm_frame = ctk.CTkFrame(master=self.options_frame, fg_color="transparent")
        self.uniterm_frame.pack(pady=10, side=ctk.TOP)

        self.first_uniterm = ctk.CTkRadioButton(master=self.uniterm_frame, text="Lewy", variable=self.uniterm_value,
                                                value=0)
        self.first_uniterm.pack(side=ctk.LEFT)
        self.second_uniterm = ctk.CTkRadioButton(master=self.uniterm_frame, text="Prawy", variable=self.uniterm_value,
                                                 value=1, width=35)
        self.second_uniterm.pack(side=ctk.RIGHT)

        self.uniterm_to_transform_header = ctk.CTkLabel(master=self.options_frame, text="Uniterm do transformacji")
        self.uniterm_to_transform_header.pack()

        self.uniterm_to_transform_frame = ctk.CTkFrame(master=self.options_frame, fg_color="transparent")
        self.uniterm_to_transform_frame.pack(pady=10, side=ctk.TOP)

        self.trans_first_uniterm = ctk.CTkRadioButton(master=self.uniterm_to_transform_frame, text="Lewy", value=0,
                                                      variable=self.uniterm_to_transform)
        self.trans_first_uniterm.pack(side=ctk.LEFT)
        self.trans_sec_uniterm = ctk.CTkRadioButton(master=self.uniterm_to_transform_frame, text="Prawy", value=1,
                                                    variable=self.uniterm_to_transform, width=35)
        self.trans_sec_uniterm.pack(side=ctk.RIGHT)

        def draw_uniterm(canv: ctk.CTkCanvas, uniterm):
            canv.delete("uniterm")
            text = canv.create_text(200, 200, text=uniterm, fill="black", font="Arial 14 bold", tags="uniterm")
            bbox = canv.bbox(text)
            if self.uniterm_value.get() == 0:
                canv.create_arc(bbox[0] - 20, bbox[1] - 30, bbox[2], bbox[3] + 10, start=120, extent=120,
                                style="arc", tags="uniterm")
            elif self.uniterm_value.get() == 1:
                canv.create_line((bbox[0] - 10, bbox[1] - 20, bbox[0] - 10, bbox[3]), tags="uniterm")
                canv.create_line((bbox[0] - 30, bbox[1] - 20, bbox[2], bbox[1] - 20), tags="uniterm")
                canv.create_line((bbox[0] - 30, bbox[3], bbox[2], bbox[3]), tags="uniterm")


        def choose_uniterm():
            val = self.uniterm_value.get()
            first_param = self.first_param_input.get()
            separator = self.sep_value.get()
            second_param = self.sec_param_input.get()
            self.uniterms[val] = [first_param, separator, second_param]
            uniterm_text = ""
            for item in self.uniterms[val]:
                uniterm_text = uniterm_text + str(item) + "\n"
            if self.uniterms[val][0] == "" or self.uniterms[val][2] == "":
                messagebox.showinfo("Uniterm", "Uniterm wymaga dwóch parametrów!")
            else:
                if val == 0:
                    draw_uniterm(self.left_drawing_frame.canvas, uniterm_text)
                elif val == 1:
                    draw_uniterm(self.right_drawing_frame.canvas, uniterm_text)
                final_canv = self.bottom_drawing_frame.canvas
                final_canv.delete("uniterm")
                if 0 in self.uniterms and 1 in self.uniterms:
                    if self.uniterm_to_transform.get() == 0:
                        first_uniterm_text = ""
                        second_uniterm_text = "\n" + self.uniterms[0][1] + "\n" + self.uniterms[0][2]
                        for item in self.uniterms[1]:
                            first_uniterm_text = first_uniterm_text + str(item) + "\n"
                        final_uniterm_text = first_uniterm_text + second_uniterm_text
                        final_canv.create_text(400, 200, text=final_uniterm_text, font="Arial 14 bold",
                                               tags="uniterm")
                        bbox = final_canv.bbox("uniterm")
                        final_canv.create_arc(bbox[0]-40, bbox[1]-20, bbox[2], bbox[3]+20, start=120, extent=120,
                                              style="arc", tags="uniterm")
                        final_canv.create_line((bbox[0] - 10, bbox[1] - 5, bbox[0] - 10, bbox[3] - 60), tags="uniterm")
                        final_canv.create_line((bbox[0] - 20, bbox[1] - 5, bbox[2] + 5, bbox[1] - 5), tags="uniterm")
                        final_canv.create_line((bbox[0] - 20, bbox[3] - 60, bbox[2] + 5, bbox[3] - 60), tags="uniterm")

                        print("Left uniterm: ", final_canv.bbox("uniterm"))

                    elif self.uniterm_to_transform.get() == 1:
                        first_uniterm_text = self.uniterms[0][0] + "\n" + self.uniterms[0][1] + "\n"
                        second_uniterm_text = "\n"
                        for item in self.uniterms[1]:
                            second_uniterm_text = second_uniterm_text + str(item) + "\n"
                        final_uniterm_text = first_uniterm_text + second_uniterm_text.rstrip()
                        final_canv.create_text(400, 200, text=final_uniterm_text, font="Arial 14 bold",
                                               tags="uniterm")
                        bbox = final_canv.bbox("uniterm")
                        final_canv.create_arc(bbox[0]-40, bbox[1]-20, bbox[2], bbox[3]+20, start=120, extent=120,
                                              style="arc", tags="uniterm")
                        final_canv.create_line((bbox[0] - 10, bbox[1]+60, bbox[0] - 10, bbox[3]+10), tags="uniterm")
                        final_canv.create_line((bbox[0] - 20, bbox[1]+60, bbox[2]+5, bbox[1]+60), tags="uniterm")
                        final_canv.create_line((bbox[0] - 20, bbox[3]+10, bbox[2]+5, bbox[3]+10), tags="uniterm")

                        print("Right uniterm: ", final_canv.bbox("uniterm"))

        self.add_uniterm = ctk.CTkButton(master=self.options_frame, text="Dodaj uniterm",
                                         command=choose_uniterm)
        self.add_uniterm.pack(pady=10)


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
