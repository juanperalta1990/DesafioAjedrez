import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Sistem")  
customtkinter.set_default_color_theme("green")  


class App(customtkinter.CTk):

    WIDTH = 950
    HEIGHT = 712

    def __init__(self):
        super().__init__()

        self.title("Desafío Ajedrez")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}+20+20")
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left "MENU" ============

        # configure grid layout (1x11)
        frame_left.grid_rowconfigure(12, weight=1)
        
        # variabels
        self.radio_var = tkinter.IntVar()
        colors = ['Blanco','Negro','Azul','Rojo','Verde']

        # widgets
        label1 = customtkinter.CTkLabel(master=frame_left,
                                              text="Pintá tu Tablero de Ajedrez",
                                              text_font=("Roboto Medium", -16)) 
        label1.grid(row=1, column=0, pady=10, padx=10)

        label2 = customtkinter.CTkLabel(master=frame_left,
                                              text="Color 1",
                                              text_font=("Roboto Medium", -14)) 
        label2.grid(row=2, column=0, padx=10)

        self.combobox1 = customtkinter.CTkComboBox(master=frame_left,
                                     values=colors,)
        self.combobox1.grid(row=3 , column=0, pady=10, padx=10)      

        label3 = customtkinter.CTkLabel(master=frame_left,
                                              text="Color 2",
                                              text_font=("Roboto Medium", -14)) 
        label3.grid(row=4, column=0, padx=10)

        self.combobox2 = customtkinter.CTkComboBox(master=frame_left,
                                     values=colors,)
        self.combobox2.grid(row=5 , column=0, pady=10, padx=10)  

        label4 = customtkinter.CTkLabel(master=frame_left,
                                              text="Selecciona el Tamaño",
                                              text_font=("Roboto Medium", -14)) 
        label4.grid(row=6, column=0, padx=10)       
        
        radio_button_1 = customtkinter.CTkRadioButton(master=frame_left,
                                                           text="8x8",
                                                           variable=self.radio_var,
                                                           value=0)
        radio_button_1.grid(row=8, column=0, pady=10, padx=30, sticky="w")

        radio_button_2 = customtkinter.CTkRadioButton(master=frame_left,
                                                           text="100x100",
                                                           variable=self.radio_var,
                                                           value=1)
        radio_button_2.grid(row=9, column=0, pady=10, padx=30, sticky="w")

        radio_button_3 = customtkinter.CTkRadioButton(master=frame_left,
                                                           text="1000x1000",
                                                           variable=self.radio_var,
                                                           value=2)
        radio_button_3.grid(row=10, column=0, pady=10, padx=30, sticky="w")


        button = customtkinter.CTkButton(master=frame_left,
                                                text="Crear",
                                                fg_color=("gray75", "gray30"),
                                                command=lambda:self.create())
        button.grid(row=11, column=0, pady=10, padx=20)

        self.switch = customtkinter.CTkSwitch(master=frame_left,
                                                text="Tema Claro / Oscuro",
                                                command=self.change_mode)
        self.switch.grid(row=12, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right TABLERO ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure(0, weight=1)
        self.frame_right.columnconfigure(0, weight=1)
        
        # set default values
        self.combobox1.set('Azul')
        self.combobox2.set('Rojo')
        radio_button_1.select()
        self.switch.select(1)
        
    def create(self):
        colors = {'Blanco': 'white', 'Negro': 'black','Azul': 'blue','Rojo': 'red','Verde': 'green'}

        if self.radio_var.get() == 0:
            num=8
            color1= colors[self.combobox1.get()]
            color2= colors[self.combobox2.get()]
            self.draw(num, color1, color2)
                        
        elif self.radio_var.get() == 1:
            num=100
            color1= colors[self.combobox1.get()]
            color2= colors[self.combobox2.get()]
            self.draw(num, color1, color2)
            
        else:
            num=1000
            color1= colors[self.combobox1.get()]
            color2= colors[self.combobox2.get()]
            self.draw(num, color1, color2)
            

    def draw(self, num, color1, color2):
        table = tkinter.Canvas(master=self.frame_right, scrollregion=(0,0,5050,5050))
        table.grid(row=0, column=0, sticky="nswe")
        box_size= 840/num
        if num > 100:
            box_size= 5000/num
            hbar=tkinter.Scrollbar(self.frame_right, orient='horizontal')
            hbar.grid(row=1, column=0, sticky='we')
            hbar.config(command=table.xview)
            vbar=tkinter.Scrollbar(self.frame_right, orient='vertical')
            vbar.grid(row=0, column=1, sticky='ns')
            vbar.config(command=table.yview)
            table.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        color = ''
        k = 0

        for j in range(num):
            for i in range(num):
                color = color1

                if k < i:
                    color = color2
                
                x1, y1 = i * box_size, j * box_size
                x2, y2 = x1 + box_size, y1 + box_size 
                table.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,)

            k += 1

        return

                
    def change_mode(self):
        if self.switch.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()

## tablero estilo ajedrez
# for j in range(num):
        #     for i in range(num):

        #         if j % 2 == 0:
        #             if i % 2 == 0:
        #                 color=color1
        #             else:
        #                 color=color2
        #         else:
        #             if i % 2 == 0:
        #                 color=color2
        #             else:
        #                 color=color1

        #         x1, y1 = i * box_size, j * box_size
        #         x2, y2 = x1 + box_size, y1 + box_size 
        #         table.create_rectangle(
        #             x1, y1, x2, y2,
        #             fill=color,)

        # return